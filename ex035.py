'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''
r1 = float(input('Digite o comprimento da RETA 1:'))
r2 = float(input('Digite o comprimento da RETA 2:'))
r3 = float(input('Digite o comprimento da RETA 3:'))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('As retas podem formar um triângulo SIM!')
else:
    print('As retas NÃO podem formar um triângulo!')
