# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('quanto dinheiro você tem na carteira? R$'))
dólar = real / 5
print('com R${} você pode comprar US${} e EU{}'.format(real, dólar))