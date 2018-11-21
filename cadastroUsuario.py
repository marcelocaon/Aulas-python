from datetime import date

print('-'*19)
print('Cadastro de Usuário')
print('-'*19)

sair= 'S'

while (sair in 'Ss'):

    nome= str(input('Digite seu nome: '))
    while nome.__len__() < 3:
        print('Digite um nome com mais de 3 caracteres...')
        nome = str(input('Digite seu nome: '))

    cpf= str(input('Digite seu cpf: '))
    while cpf.isdigit() == False:
        print('digite somente números...')
        cpf = str(input('Digite seu cpf: '))
    while cpf.__len__() != 11 :
        print ('cpf incorreto...')
        cpf = str(input('Digite seu cpf: '))

    data= str(input('Digite sua data de nascimento: xx/xx/xxxx '))

    email= input('Digite seu email: ')
    while '@' not in email:
        print('Por favor, digite um email válido...')
        email = input('Digite seu email: ')

    sair= input ('Informar os dados novamente? ')

#Converte o padrao de data americano para o brasileiro
# data_atual = date.today()
# print(data_atual)
# data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
# data_atual.year)
#data_em_texto = data_atual.strftime(‘%d/%m/%Y’)
#print(data_em_texto)