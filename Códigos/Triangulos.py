a = int(input("Lado a:"))
b = int(input("Lado b:"))
c = int(input("Lado c:"))

if (a+b+c) or (a+c<b) or (b+c<a):
    print("Não é um triangulo")
else:
    if(a==b==c):
        print("Equilatero")
    elif(a==b) or (a==c) or (b==c):
        print("Isoceles")
    else:
        print("Escaleno")