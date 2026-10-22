from math import radians, sin, cos, tan
ang = float (input('Digite um angulo qualquer: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo {} tem os sguintes valores:\n'
      'Seno = {:.3f}\n'
      'Cosseno = {:.3f}\n'
      'Tangente = {:.3f}'.format(ang, seno, cosseno, tangente))
