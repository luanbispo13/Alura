# Coleta e amostragem de dados

# 1. Solicita o nome da pessoa usuária e exibe uma saudação
Nome = input('Digite seu nome: ')
print(f'Olá, {Nome}.')

# 2. Solicita o nome e idade e exibe a mensagem formatada
Nome = input('\nDigite seu nome: ')
Idade = int(input('Digite sua idade: '))
print(f'Olá {Nome}, você tem {Idade} anos.')

# 3. Solicita o nome, idade e altura e exibe a mensagem formatada
Nome = input('\nDigite seu nome: ')
Idade = int(input('Digite sua idade: '))
Altura = float(input('Digite sua altura: '))
print(f'Olá {Nome}, você tem {Idade} anos e mede {Altura} metros!')


# Calculadora com operadores

# 1. Soma de dois valores
A = int(input('\nDigite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
print('Soma:', A + B)

# 2. Soma de três valores
A = int(input('\nDigite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))
print('Soma:', A + B + C)

# 3. Subtração entre dois valores
A = int(input('\nDigite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
print('Subtração:', A - B)

# 4. Multiplicação entre dois valores
A = int(input('\nDigite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
print('Multiplicação:', A * B)

# 5. Divisão (verificando denominador diferente de zero)
Numerador = int(input('\nDigite o numerador: '))
Denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print('Divisão:', Numerador / Denominador)

# 6. Exponenciação
Operador = int(input('\nDigite o operador valor: '))
Potencia = int(input('Digite a potência valor: '))
print('Resultado da exponenciação:', Operador ** Potencia)

# 7. Divisão inteira
Numerador = int(input('\nDigite o numerador: '))
Denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print('Divisão inteira:', Numerador // Denominador)

# 8. Resto da divisão
Numerador = int(input('\nDigite o numerador: '))
Denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print('Resto da divisão:', Numerador % Denominador)

# 9. Média de 3 notas
Nota1 = float(input('\nDigite a 1ª nota: '))
Nota2 = float(input('Digite a 2ª nota: '))
Nota3 = float(input('Digite a 3ª nota: '))
print(f'Média: {(Nota1 + Nota2 + Nota3) / 3}')

# 10. Média ponderada fixa
MediaPonderada = (5*1 + 12*2 + 20*3 + 15*4) / (1 + 2 + 3 + 4)
print(f'\nMédia ponderada: {MediaPonderada}')


# Editando textos

# 1. Frase pré-definida
Frase = 'Olá Python!'
print('\n', Frase)

# 2. Solicita frase e imprime
Frase = input('\nDigite uma frase: ')
print(Frase)

# 3. Frase em maiúsculas
Frase = input('\nDigite uma frase: ')
print(Frase.upper())

# 4. Frase em minúsculas
Frase = input('\nDigite uma frase: ')
print(Frase.lower())

# 5. Frase com espaços no início e fim (pré-definida)
Frase = '  Olá Python!  '
print('\nFrase sem espaços:', Frase.strip())

# 6. Remover espaços do início e fim (digitada)
Frase = input('\nDigite uma frase: ')
print(Frase.strip())

# 7. Remover espaços e deixar tudo minúsculo
Frase = input('\nDigite uma frase: ')
print(Frase.strip().lower())

# 8. Trocar todas as vogais “e” por “f”
Frase = input('\nDigite uma frase: ')
print(Frase.lower().replace('e', 'f'))

# 9. Trocar todas as vogais “a” por “@”
Frase = input('\nDigite uma frase: ')
print(Frase.lower().replace('a', chr(64)))

# 10. Trocar todas as consoantes “s” por “$”
Frase = input('\nDigite uma frase: ')
print(Frase.lower().replace('s', chr(36)))

print('\nFim das atividades!')