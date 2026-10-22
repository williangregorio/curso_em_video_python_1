# faça o computador pensar em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
from time import sleep
from random import randint

numero = randint(0, 5)
print('#'*70)
usuario = int(input("Tente adivinhar o número que estou pensando (entre 0 e 5): "))
print('#' *70)
print("PROCESSANDO...")
sleep(2)

if usuario == numero:
    print("Parabéns! Você acertou!")
else:
    print("Que pena! Eu Venci! O número era {} e não {}!".format(numero, usuario))