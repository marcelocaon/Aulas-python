import random

print('---JOQUEMPÔ--- >> Pedra, Papel e Tesoura <<\n')

print('-'*10)
print('1 = Pedra \n2 = Papel \n3 = Tesoura')
print('-'*10)
n= int(input('\nDigite: '))

if (n== 1):
    jogador= 'Pedra'
elif (n== 2):
    jogador= 'Papel'
elif (n== 3):
    jogador= 'Tesoura'

print('1, 2, 3, JOQUEMPÕ...')
lista=['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)
print('Eu joguei {}'.format(computador))
print('Voce jogou {}'.format(jogador))

if (computador== 'Pedra' and jogador== 'Pedra'):
    print('Empatou...')
elif (computador== 'Papel' and jogador== 'Papel'):
    print('Empatou...')
elif (computador== 'Tesoura' and jogador== 'Tesoura'):
    print('Empatou...')
elif (computador== 'Pedra' and jogador== 'Papel'):
    print('Voce ganhou, PARABÉNS...')
elif (computador == 'Papel' and jogador == 'Tesoura'):
    print('Voce ganhou, PARABÉNS...')
elif (computador == 'Tesoura' and jogador == 'Pedra'):
    print('Voce ganhou, PARABÉNS...')
elif (computador== 'Pedra' and jogador== 'Tesoura'):
    print('Eu ganhei, PARABÉNS pra mim...')
elif (computador == 'Papel' and jogador == 'Pedra'):
    print('Eu ganhei, PARABÉNS pra mim...')
elif (computador == 'Tesoura' and jogador == 'Papel'):
    print('Eu ganhei, PARABÉNS pra mim...')


