# crie um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
dias = int(input('quantos dias alugados? '))
km = float(input('quantos Km rodados? '))

# calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 0.15 por Km.
pago = (dias * 60) + (km * 0.15)

print('o total a pagar é R${:.2f}'.format(pago))