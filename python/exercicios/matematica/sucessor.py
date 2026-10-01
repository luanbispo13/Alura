# crie um programa que leia 1 número inteiro e mostre na tela seu sucessor e antecessor

n = int(input('digite algum número: '))
antecessor = n - 1
sucessor = n + 1

print('analisando o valor {}. \nseu antecessor é {}. \nseu sucessor é {}.'.format(n, antecessor, sucessor))