titulo = "Tabuada FOR"
print(f"{titulo:^30}")
i = 1
num = int(input("Entre com um número"))
for i in range(1,11):
    tabuada = num * i
    print(f"{i} X {num} = {tabuada}")
