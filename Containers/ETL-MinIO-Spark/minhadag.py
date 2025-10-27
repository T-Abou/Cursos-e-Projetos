from airflow import DAG
from airflow.operators.python import PythonOperator
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, date_format
from minio import Minio
import pendulum
import logging
import glob
import io
import os
import shutil


# --- Configurações globais ---
BASE_RAW_PATH = "/opt/airflow/data/raw"
BUCKET_NAME = "balde-teste2"

SOURCE_FILES = {
    "clientes": "clientes.csv",
    "vendas": "vendas.csv",
    "campanhas": "campanhas.csv"
}


# --- Função para criar SparkSession ---
def _get_spark_session(app_name: str) -> SparkSession:
    logging.info(f"Iniciando SparkSession para {app_name}")
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.master", "local[*]") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark


# --- Função para processar e enviar Parquet ao MinIO ---
def process_and_save_to_s3(source_file_name: str, **kwargs):
    logging.info(f"Iniciando processamento do arquivo {source_file_name}")
    local_file_path = f"{BASE_RAW_PATH}/{source_file_name}"

    if not os.path.exists(local_file_path):
        logging.error(f"Arquivo {local_file_path} não encontrado!")
        return

    spark = _get_spark_session(f"Process_{source_file_name}")

    try:
        df = spark.read.csv(local_file_path, header=True, inferSchema=True)
        logging.info(f"Arquivo {source_file_name} lido com {df.count()} linhas")

        df_clean = df.dropna()
        logging.info(f"{df_clean.count()} linhas após remoção de nulos")

        # --- Separar Data e Hora apenas para vendas.csv ---
        if source_file_name == "vendas.csv":
            # Cria coluna Hora a partir da Data original
            df_clean = df_clean.withColumn("Hora", date_format(col("Data"), "HH:mm:ss"))
            # Agora transforma Data em só data (remove hora)
            df_clean = df_clean.withColumn("Data", to_date(col("Data")))

        temp_dir = "/tmp/temp_parquet"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)

        df_clean.coalesce(1).write.mode("overwrite").parquet(temp_dir)
        parquet_file = glob.glob(f"{temp_dir}/part-*")[0]

        client = Minio(
            "minio:9000",
            access_key="minioadmin",
            secret_key="minioadmin",
            secure=False
        )

        object_name = f"processed/{source_file_name.replace('.csv', '.parquet')}"
        client.fput_object(BUCKET_NAME, object_name, parquet_file)
        logging.info(f"Arquivo salvo no MinIO como {object_name}")

    finally:
        spark.stop()
        logging.info(f"SparkSession finalizado para {source_file_name}")
        if 'temp_dir' in locals() and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


# --- Definição da DAG ---
with DAG(
    dag_id='Etl_Spark_MinIO',
    start_date=pendulum.datetime(2025, 10, 16, tz="UTC"),
    schedule=None,
    catchup=False,
    max_active_tasks=1,
    tags=['spark', 'minio', 'etl']
) as dag:

    tasks = []
    for file_type, file_name in SOURCE_FILES.items():
        task = PythonOperator(
            task_id=f'processar_{file_type}',
            python_callable=process_and_save_to_s3,
            op_kwargs={'source_file_name': file_name},
        )
        tasks.append(task)

    for task in tasks:
        task
