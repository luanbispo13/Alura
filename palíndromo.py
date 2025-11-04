# Crie um programa que verifica se uma palavra é palíndromo.

palavra = input("digite uma palavra: ")

if palavra == palavra[::-1]:
    print("é um palíndromo.")

else:
    print("não é um palíndromo.")