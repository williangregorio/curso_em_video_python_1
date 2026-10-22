frase = str(input('Digite uma frase: ')).strip().upper()
qtd_letras = frase.count('A')
primeira_posicao = frase.find('A')+1
ultima_posicao = frase.rfind('A')+1
print('A frase digitada contem {} letras, onde {} são letras A \nA primeira letra A aparece na posição {} \n'
      'A última letra A aparece na posição {}'.format(len(frase),qtd_letras,primeira_posicao,ultima_posicao))
