cardapio = []
while True:
    comida = input("Entre com a comida ou 0 para sair")
    if comida[0] == '0':
        break
    cardapio.append(comida)
print(cardapio)

cardapio = tuple(cardapio)
cardapio = list(cardapio)

if "Queijo Roquefort" in cardapio:
    indice = cardapio.index("Queijo Roquefort")
    cardapio.insert(indice + 1, "Azeitona")

print(cardapio)

ultimos3 = cardapio[-3:]
print(ultimos3)

lista_temp =[]

for item in ultimos3:
    lista_temp.append([item,input(f"Digite a quantidade para {item}")])
print(lista_temp)

lista = tuple(lista_temp)
print(lista)





