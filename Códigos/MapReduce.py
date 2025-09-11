# Funcoes

#Com numero de parametro variaveis

def soma(*numeros):
    #qdo tem um asterisco, ele devolve uma tupla
    soma = 0
    for numero in numeros:
        soma+= numero
    return(soma)

print(soma(3,5,6))
print(soma(56,3,1,6,8,91,2))

def dobro (p):
    return p*2
print(dobro(6))

numeros = [56,3,1,6,8,91,2]
numerosdobrados = []
for numero in numeros:
    numerosdobrados.append(dobro(numero))
print(f'Numeros {numeros}')
print(f'Numeros {numerosdobrados}')
numerosdobradosmap = list(map(dobro,numeros))
print(numerosdobradosmap)

#reduce
#o reduce junta todos os elementos da lista de acordo com uma funcao
def soma2 (n1,n2):
    return n1 + n2
numeros = [56,3,1,6,8,91,2]
somatotal = 0
for numero in numeros:
    somatotal = soma2(somatotal,numero)
print(f'A soma total de {numeros} é {somatotal}')


from functools import reduce
print(f'A soma total de {numeros} é {reduce(soma2,numeros)}')

letras = ['T','i','a','g','o']
somaletras = ''
def somaletras (n1,n2):
    return n1 + n2
print(f'A soma total de {str(letras)} é {str(reduce(somaletras,letras))}')

#Com map
listaOriginal = [234,64,13467,45.89,23]
def desconto (p):
    return round(p * 0.8, 2)
listacomdesconto = list(map(desconto,listaOriginal))
print(f'teste {listacomdesconto}')

valor_descontado = []
for numero in range(len(listaOriginal)):
    valor_descontado.append(round(listaOriginal[numero] - listacomdesconto[numero], 2))
print(f'o valor descontado foi {valor_descontado}')



#Sem map
# listadescvazia= []
# for numero in listaOriginal:
#     listadescvazia.append(round(desconto(numero), 2))
# print(f'Numeros {listaOriginal}')
# print(f'Numeros {listadescvazia}')


#Escrevendo a mesma função em labda

#Aqui usamos a funcao lambda nomeada quando no codigo vamos usar mais de uma vez
soma2lambda = lambda n1,n2 : n1 + n2
print(soma2lambda(4,2))

print((lambda n1,n2:n1+n2)(8,9))

#fazendo lamda com descontos

listaOriginal = [234,64,13467,45.89,23]
listaDescontos = [0.3,0.004,0.5,0.03,0.8]

print(f'preços originais:\n {listaOriginal}')

print(f'preço com desconto \n'
      f'{list(map((lambda p,d: round(p*(1-d),2)),[234,64,13467,45.89,23],[0.3,0.004,0.5,0.03,0.8]))}')


def mult2_100(n):
    if n < 10:
        return n*2
    else:
        return n*100

print(f'teste 6: {mult2_100(6)}')
print(f'teste 12: {mult2_100(12)}')

#fazendo com lambda
lmult2_100 = lambda n : n*2 if n<=10 else n*100
print(f'teste 6: {lmult2_100(6)}')
print(f'teste 12: {lmult2_100(12)}')

#Volume esfera
# raio = float(input('Qual o raio da esfera'))
# volume = (lambda r: 4/3 * 3.14159268 * r**3)(raio)
# print(f'O volume da esfera de raio {raio} é {round(volume,2)}')


#media da lista
listaOriginal = [234,64,13467,45.89,23]

print(f'A média da lista é:{(lambda lista: sum(lista)//len(lista))(listaOriginal)}')

#List comprehension
numeros1a5  = [i for i in range(1,6)]
print(numeros1a5)

numerospares1a100 = [i for i in range(1,101) if i %2 ==0]
print(numerospares1a100)

numeros1a100paresenegativos = [i if i%2 == 0 else -i for i in range(1,101)]
print(numeros1a100paresenegativos)

#Exercicios list Comprehesion
lOriginal = [' vermelho',' verde', 'azul ', 'amarelo ']
lSemespaco = [cor.strip() for cor in lOriginal]
print(lSemespaco)

cores = ['vermelho', 'verde', 'azul', 'amarelo']
coresporlinha = [print(cor.strip()) for cor in lOriginal]

numnegativo = [-4,-2,0,2,4]
semnegativo = [i for i in numnegativo if i >= 0]
print(semnegativo)

iMix = [-4,'v','X','cacto',-2,0,'y',2,4]
semnum = [item for item in iMix if isinstance(item, (int, float))]
print(semnum)

# Quadrados dos numeros de 1 a 10
print({i: i**2 for i in range(1,11)})

#contar quantas vezes aparece a letra em uma palavra
palavra = 'banana'
contagem = {i: palavra.count(i) for i in palavra}
print(contagem)

alunos = {"Ana":10,"Bruno":8,"Carla":9}
inverso = {i: chave for chave, i in alunos.items()}
print(inverso)

#DESAFIO
#Dada a lista abaixo gere uma nova lista e faça as operações
#Some os numeros de cada sublista com lambda
#se a lista estiver vazia retorne zero
#so manter os resultados pares
#elevar ao quadrado cada resultado

lista = [[1,2,3],[4,5,6],[7],[],[8,9][10]]
