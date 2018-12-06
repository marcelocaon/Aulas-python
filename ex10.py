import random, emoji


print('---Escolha um número de 1 a 10---')

lista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha= random.choice(lista)

tentar= 's'
while (tentar == 's' or tentar == 'S'):
    n = int(input('Digite um número: '))

    if (n == escolha):
        print(emoji.emojize('Voce acertou o número, Parabéns...:clap:', use_aliases=True))
        tentar = input('Jogar novamente? (s / n)')
        escolha = random.choice(lista)
    else:
        #print('Voce errou')
        print(emoji.emojize('Voce errou :anguished:', use_aliases=True))

        tentar= input('Tentar novamente? (s / n)')
