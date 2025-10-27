FROM apache/airflow:3.1.0

USER root

# Instala Java e dependências do sistema
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk-headless \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Configura o Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Volta para o usuário airflow para instalar pacotes Python
USER airflow

# Instala pacotes Python necessários
RUN pip install --no-cache-dir \
	pyspark==3.5.7 \
    minio \
    apache-airflow-providers-amazon==7.2.0
