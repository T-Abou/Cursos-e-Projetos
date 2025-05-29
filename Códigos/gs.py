tipos_desastre = []
paises = []
cidades = []
bairros = []
ruas = []

total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

quantidade = int(input("Quantos desastres foram registrados? "))

for i in range(quantidade):
    print(f"\nDados do Desastre {i + 1}")

    tipo = input("Tipo de desastre: ")
    pais = input("Em qual país: ")
    cidade = input("Em qual cidade: ")
    bairro = input("Em qual bairro: ")
    rua = input("Em qual rua: ")

    tipos_desastre.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)

    while True:
        total = int(input("Quantidade TOTAL de pessoas afetadas: "))
        qtd_criancas_afet = int(input("Quantidade de crianças: "))
        qtd_adultos_afet = int(input("Quantidade de adultos: "))
        qtd_idosos_afet = int(input("Quantidade de idosos: "))
        qtd_mobilidade_afet = int(input("Quantidade de pessoas com mobilidade reduzida: "))
        qtd_feridos_afet = int(input("Quantidade de feridos: "))

        soma = qtd_criancas_afet + qtd_adultos_afet + qtd_idosos_afet + qtd_mobilidade_afet + qtd_feridos_afet

        if soma == total:
            total_afetados.append(total)
            criancas.append(qtd_criancas_afet)
            adultos.append(qtd_adultos_afet)
            idosos.append(qtd_idosos_afet)
            mobilidade_reduzida.append(qtd_mobilidade_afet)
            feridos.append(qtd_feridos_afet)
            break
        else:
            print("\nERRO: A soma das categorias NÃO corresponde ao total de pessoas afetadas.")
            print(f"\nSoma das categorias = {soma}, mas o total informado foi {total}")
            print("\nPor favor, preencha os dados corretamente")

print("\n\n== RELATÓRIO DOS DESASTRES REGISTRADOS ==")
for i in range(quantidade):
    print(f"\n Desastre {i + 1} ")
    print(f"Tipo: {tipos_desastre[i]}")
    print(f"Rua {ruas[i]} ")
    print(f"Bairro: {bairros[i]} ")
    print(f"Cidade: {cidades[i]} ")
    print(f"País: {paises[i]}")
    print(f"Total de pessoas afetadas: {total_afetados[i]}")
    print(f"  - Crianças: {criancas[i]}")
    print(f"  - Adultos: {adultos[i]}")
    print(f"  - Idosos: {idosos[i]}")
    print(f"  - Pessoas com mobilidade reduzida: {mobilidade_reduzida[i]}")
    print(f"  - Feridos: {feridos[i]}")

#relatorio

#A-)
print(f"\nQuantidade de desastres registrados:{quantidade}")

#B-)
total_geral_afetados = sum(total_afetados)
print(f" Total geral de pessoas afetadas: {total_geral_afetados}")

#C-)
total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

print(" Total por categoria:")
print(f"  - Crianças: {total_criancas}")
print(f"  - Adultos: {total_adultos}")
print(f"  - Idosos: {total_idosos}")
print(f"  - Pessoas com mobilidade reduzida: {total_mobilidade}")
print(f"  - Feridos: {total_feridos}")

#D-)
categorias = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Pessoas com mobilidade reduzida": total_mobilidade,
    "Feridos": total_feridos
}

categoria_mais_afetada = max(categorias, key=categorias.get)
print(f"\nCategoria mais afetada no geral: {categoria_mais_afetada} ({categorias[categoria_mais_afetada]} pessoas)")

#E-)
maior_afetados = max(total_afetados)
indice_maior = total_afetados.index(maior_afetados)

print("\nDesastre com maior número de afetados:")
print(f"  - Tipo: {tipos_desastre[indice_maior]}")
print(f"  - Localização: País:{paises[indice_maior]} | Cidade: {cidades[indice_maior]} | Bairro: {bairros[indice_maior]} | Rua: {ruas[indice_maior]}")
print(f"  - Total de afetados: {maior_afetados}")




