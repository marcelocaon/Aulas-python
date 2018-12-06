print('-'*22)
print('Sequencia de Fibonacci') #Eh a soma dos dois numeros anteriores p.e. 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13...
print('-'*22)

qtd= int(input('Quantos termos voce quer? '))

termo1= 0 #primeiro termo eh sempre zero
termo2= 1 #segundo termo eh sempre 1

if qtd ==1:
    print('*'*30)
    print('{}'.format(termo1), end='') #end='' no final eh para nao pular linha
elif qtd ==2:
    print('*'*30)
    print('{} - {}'.format(termo1,termo2), end='')
else:
    contador= 3 #pq a primeira e segunda posicoes eu ja sei obrigatoriamente como 0 e 1
    print('*' * 30)
    print('{} - {}'.format(termo1, termo2), end='')
    while contador <= qtd:
        termo3= termo1 + termo2
        print(' - {}'.format(termo3),end='')
        termo1= termo2
        termo2= termo3
        contador += 1 #mesmo que contador= contador + 1
print(' FIM')