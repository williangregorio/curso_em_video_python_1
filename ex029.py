# radar eletrônico
velocidade = float(input('Qual a velocidade que o carro está trafegando? '))
if velocidade < 80:
    print('Parabéns!')
else:
    print('Você está acima da velocidade permitida de 80km/h! \n'
          'E por isso será multado em: R${:.2f}'.format((velocidade-80)*7))
print('Dirija com cuidado e segurança e tenha uma ótima viagem!')
