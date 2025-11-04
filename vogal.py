# crie um código que conta o número de vogais em 1 palavra

palavra = input('digite uma palavra: ')
vogais = 'aeiouAEIOU'
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print('número de vogais: {}'.format(contador))