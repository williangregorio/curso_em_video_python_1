valor = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = float(valor / 3.27)
print('Com R${:.2f} é possível comprar US${:.2f}'.format(valor,dolar))
