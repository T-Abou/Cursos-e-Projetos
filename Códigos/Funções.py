#Funções

#Reaproveitaveis

#Em algumas linguagens existem diferenças entre funções e procedimentos
#procedimento não retorna valor
#função retorna valor

#Boa pratica é criar funções no começo do arquivo ou colocar em arquivos/bibliotecas separadas

#1º parte
#def OlaMundo():

#2º usar função
#OlaMundo()

#Escopo

def soma():
    xpto = 1+2
    print(xpto)
soma()

ypto = 0
def soma1():
    ypto = 5+4
    print(ypto)
soma1()

def impressao(p):
    print(f'O valor do meu paramentro é ',p)
impressao('Boa tarde')
impressao(2)

#Parametros Default
def somapadrao(n1, n2=100):
    soma = n1 + n2
    print(f'a soma de {n1} e {n2} é {soma}')
somapadrao(2, 4)
somapadrao(67)

def parametros(p1,p2,p3,p4,p5=10,p6=20,p7=-9):
    print(p1,p2,p3,p4,p5,p6,p7)
parametros(1,3,6,7)

def soma(n1,n2):
    total = n1+n2
    return total