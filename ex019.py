from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do primeiro aluno: '))
aluno4 = str(input('Digite o nome do segundo aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('O professor escolheu o aluno {} para limpar o quandro'.format(choice([aluno1,aluno2,aluno3,aluno4])))
print('Outra forma de escolher é usando lista. O escolhido foi: {}'.format(choice(lista)))