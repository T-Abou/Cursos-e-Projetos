titulo = "divisivel por número"
print(titulo)
n = int(input("Entre com um número:"))
for i in range (1,101):
    if i % n == 0:
        print(i)