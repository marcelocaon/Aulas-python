print ('Calculadora Simples')

n1 = int (input('Digite um número:'))
n2 = int (input('Digite outro número:'))

tipo = input('Digite a operação (+ para somar, - para diminuir, * para multiplicar, / para dividir):')

if tipo == '+':
    resultado = n1 + n2
elif tipo == '-':
    resultado = n1 - n2
elif tipo == '*':
    resultado = n1 * n2
elif tipo == '/':
    resultado = n1 / n2

#print ('Resultado de ', n1, tipo, n2, '= ',resultado)
#outra forma de fazer o print
print ('Resultado de {} {} {} = {}'.format (n1, tipo, n2, resultado))

