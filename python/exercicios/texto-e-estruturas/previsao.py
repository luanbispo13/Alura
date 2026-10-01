horario = input('digite a previsão do dia: ')

if horario == 'manhã':
    print('bom dia!')

elif horario == 'tarde':
    print('boa tarde!')

else:
    print('boa noite!')

for numero in range(10):
    dobro = numero * 2
    print('o dobro de {} é {}'.format(numero, dobro))