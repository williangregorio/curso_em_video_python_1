dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km o carro rodou?'))
valor_total = (dias * 60) + (km * 0.15)
print('O valor total a ser pago pelo aluguel será de R${:.2f}'.format(valor_total))
