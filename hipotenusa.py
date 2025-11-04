# crie um programa que leia o comprimento do cateto oposto e adjacente de um triângulo retângulo. calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print('hipotenusa vai medir {:.2f}'.format(hi))