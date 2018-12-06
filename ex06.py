import math

print('---Programinha para mostrar a tabuada de um numero---')

n= int(input('Digite um número: '))

contador= 0
# posso usar o operador de multiplicação para replicar uma string por uma quantidade de vezes
print('-' * 12)

while (contador < 11):
    print ('{} x {} = {}'.format(n, contador, n*contador))
    contador= contador +1
print('-' * 12)


#Ordem dos operadores aritiméticos
#1o = o que estiver dentro de parenteses
#2o = ** exponenciação
#3o = *, /, // (divisão somente inteiro) e % (resto de uma divisão
#4o = + e -