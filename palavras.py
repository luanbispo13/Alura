# Crie um programa que conta o número de palavras em uma frase.

frase = input("Digite uma frase: ")
palavras = frase.split()
num_palavras = len(palavras)
print('número de palavras na frase: {}'.format(num_palavras))
