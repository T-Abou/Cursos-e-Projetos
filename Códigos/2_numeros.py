titulo = "Divisivel por 5"
print(titulo)

n1=int(input("Entre com um número"))
n2=int(input("Entre com outro número"))

for i in range(n1, n2+1):
    if i % 5 == 0:
        print(i)