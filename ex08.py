print('---Script mostra o poder do print2---')

n1= int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))

s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2

#end no final do print colca junto a proxima linha
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a exponenciação é {}'.format(di, e))

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='>>>')
print('A divisão inteira é {} e a exponenciação é {}'.format(di, e))

#\n = pular linha
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} \n e a exponenciação é {}'.format(di, e))

