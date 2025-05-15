titulo = "Compre mercadorias"
print(f"{titulo:^30}")
preco = float(input("Qual o valor da mercadoria"))
dinheiro = float(input("Quanto dinheiro você possui"))
if dinheiro >= preco:
    print("Pode comprar")
else:
    print("Economize...")