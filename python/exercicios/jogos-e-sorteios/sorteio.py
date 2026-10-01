from random import choice
n1 = str(input('nome do primeiro aluno: '))
n2 = str(input('nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('o aluno escolhido foi: \n{}'.format(escolhido))