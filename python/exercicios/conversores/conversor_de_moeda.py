# Crie um programa que converte uma quantidade de dinheiro de uma moeda para outra.

valor_em_reais = float(input("digite o valor em reais: "))
cotacao_dolar = 5.5
valor_em_dolares = valor_em_reais / cotacao_dolar
print('valores em doláres: {}'.format(valor_em_dolares))