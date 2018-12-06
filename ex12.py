import random, emoji


print('---O número é Par ou Ímpar?---')

n= float(input('Digite um número: '))

#resto da divisão, se for 0 o numero é par se for <> 0 o numero é impar
resultado= n % 2
if (resultado == 0):
    print('O número {} é Par.'.format(n))
else:
    print('O número {} é Ímpar.'.format(n))

