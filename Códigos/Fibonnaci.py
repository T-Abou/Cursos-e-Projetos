n = int(input("Digite o valor de N: "))
a = 0
b = 1
i = 1
while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

# titulo = "Fibonacci"
# print(titulo)
# qt_termos = int(input("Entre com a quantidade de termos"))
# a,b,i = 0,1,1
#
# while i <= qt_termos:
#     if qt_termos > 2:
#         total = a+b
#     print(total)
#     #a = b
#     #b = total
#     a, b = b ,total
# elif i == 1:
#     total = a
#         print(a)
#     else:
#         total = b
#         print(b)
#     i += 1