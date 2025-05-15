titulo = "Trabalho ou Fim da Semana"
print(titulo)
dia = int(input("Entre com um número de 1 a 7:"))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _: #igual ao else
        print("Dia invalido")

match dia:
    case 2 | 3 | 4 | 5 | 6: #a barra equivale ao OR
        print("Dia de trabalho")
    case 1 | 7:
        print("Fim de semana")
    case _:
        print("Dia inválido")
