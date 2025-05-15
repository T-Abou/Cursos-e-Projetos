titulo = "Dia da semana"
print(titulo)
dia = int(input("Entre com um número de 1 a 7:"))

#if not(dia.isdigit()):
#    print("Entre com digitos")
#else:
#    dia = int(dia)

if dia ==2:
    print("Segunda")
elif dia ==3:
    print("Terça")
elif dia ==4:
    print("Quarta")
elif dia ==5:
    print("Quinta")
elif dia ==6:
    print("Sexta")
elif dia ==7:
    print("Sábado")
else:
    print("Dia invalido")