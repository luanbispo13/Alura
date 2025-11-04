# crie um programa que verifica se o número é par ou ímpar

número = int(input('digite um número: '))

if número % 2 == 0:
    print('{} é um número par.'.format(número))

else:
    print('{} é um número ímpar.'.format(número))   