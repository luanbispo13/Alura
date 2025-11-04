# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc

num = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))