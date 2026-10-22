import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('Para um triângulo que tenha as seguintes dimensões:\n'
      'Cateto Oposto: {}\n'
      'Cateto Adjacente: {}\n'
      'Sua Hipotenusa será: {:.3f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))