import math
# importando a biblioteca de matématica

n1 = int(input('digite um número: '))
raiz = math.sqrt(n1)
print('a raiz de {} é igual a {:.2f}'.format(n1, math.ceil(raiz)))

import random
# importando a biblioteca de números aleatórios
num = random.randint(1, 20)
print('o número {} foi gerado.'.format(num))

import emoji
# importando a biblioteca de emoji
print(emoji.emojize('o Luan é estudante excelente :blue_heart:'))