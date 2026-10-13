#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario_atual = float(input('Digite o salário atual: R$'))
if salario_atual > 1250:
    salario_novo = salario_atual + (salario_atual * 0.10)
else:
    salario_novo = salario_atual + (salario_atual * 0.15)
print ('O salário atual de R${:.2f} foi atualizado para R${:.2f}'.format(salario_atual, salario_novo))

