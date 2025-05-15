titulo = "Tabuada WHILE"
print(f"{titulo:^30}")
i = 1
num = int(input("Entre com um número"))
while i <= 10:
    tabuada = num * i
    print(f"{i} X {num} = {tabuada}")
    i += 1