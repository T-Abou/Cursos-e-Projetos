titulo = "Preço Mercadoria"
print(titulo)

carrinho = 10
boneca = 12
guarda_chuva = 17.50

print("preço do carrinho é R$ 10")
print("preço da boneca é R$ 12")
print("preço do guarda-chuva é R$ 17,50")

valor = float(input("Qual valor você possui em mãos? "))

if valor >= 10.99:
    if valor < 12.00:
        print("Você pode comprar apenas o carrinho")
    elif 11.00 <= valor < 17.50:
        print("Você pode comprar uma boneca ou um carrinho")
    else:
        print("Você pode escolher entre as 3 mercadorias")
else:
    print("Você não pode comprar nenhuma mercadoria")

