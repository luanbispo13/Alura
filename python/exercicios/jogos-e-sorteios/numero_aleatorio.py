# Crie um programa que gere números aleatórios.

import random  # Importa a biblioteca random.

# Solicita ao usuário que insira o valor mínimo para gerar o número aleatório.
min = int(input('Digite o valor mínimo: '))

# Solicita ao usuário que insira o valor máximo para gerar o número aleatório.
max = int(input('Digite o valor máximo: '))

# Gera um número aleatório dentro do intervalo especificado pelo usuário.
numero_aleatorio = random.randint(min, max)

# Imprime o número aleatório gerado.
print('O número aleatório é: {}'.format(numero_aleatorio))