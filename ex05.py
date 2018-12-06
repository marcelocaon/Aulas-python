import math

print('Programinha para calcular média com e sem arrendodamento')

n1= float (input('Digite o primeiro valor: '))
n2= float (input('Digite o segundo valor: '))

media= (n1 + n2) / 2
print ('A média entre {} e {} é {}'.format(n1, n2, media))

#:.1f quer dizer que apos o ponto do numero float considerar apenar uma casa decimal e arredondar
print ('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, media))