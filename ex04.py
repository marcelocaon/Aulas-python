import math

print('Programinha para dizer o Dobro, Triplo e Raiz Quadrada de um número')

n= float (input('Digite um número...'))

dobro= n*2
triplo= n*3
#raiz= n**(1/2) outra forma de calcular a raiz se fosse cubica usaria n**(1/3)
raiz= math.sqrt(n)
print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz quadrada de {} é {}'.format(n, raiz))


#math.sqrt(numero): Retorna a raíz quadrada do número.
#math.cos(numero): Retorna o cosseno do número em radiano.
#math.sin(numero): Retorna o seno do número em radiano.
#math.tan(numero): Retorna a tangente do número em radiano.
#math.radians(numero): Converte o angulo ‘numero’ de graus para radiano.
#math.pi: Não é bem uma função, está mais para uma constante com o número pi (3.1415926535897931).
#math.hypot(x, y): Retorna a hipotenusa dos números (catetos) fornecidos.