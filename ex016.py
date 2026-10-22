from math import trunc
num = float(input('Digite um número real qualquer: '))
print ('O número {} tem como inteiro o número {}'.format(num, trunc(num)))
print('Usando opção com INT para avaliar: {}'.format(int(num)))
print('Usando opção com formatação para avaliar: {:.0f}'.format(num))
