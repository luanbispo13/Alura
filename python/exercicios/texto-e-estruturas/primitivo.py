# crie um programa que leia um valor digitado pelo usuário e mostre na tela seu tipo primitivo além das outras características

aluno = input('digite algo: ')

print('tipo primitivo desse valor é {}'.format(type(aluno)))
print('tem espaço? {}'.format(aluno.isspace()))
print('é número? {}'.format(aluno.isnumeric()))
print('é alfabético? {}'.format(aluno.isalpha()))
print('é alfanúmerico? {}'.format(aluno.isalnum()))
print('tá maiúsculo? {}'.format(aluno.isupper()))
print('tá minúsculo? {}'.format(aluno.islower()))
print('tá capitalizado? {}'.format(aluno.istitle()))