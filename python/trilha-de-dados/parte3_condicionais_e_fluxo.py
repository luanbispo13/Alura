# Condicionais e Controle de Fluxo

# 1. Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
print('\n# 1. Comparação de dois números')
num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))

if num1 > num2:
    print(f'O primeiro número é maior: {num1}')
elif num2 > num1:
    print(f'O segundo número é maior: {num2}')
else:
    print('Os dois números são iguais.')

# 2. Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
print('\n# 2. Análise de crescimento/decrescimento')
variacao = float(input('Digite o percentual de crescimento (Ex: 5 para 5%, -2.5 para -2.5%): '))

if variacao > 0:
    print(f'Houve um crescimento de {variacao}%')
elif variacao < 0:
    print(f'Houve um decrescimento de {variacao}%')
else:
    print('Não houve crescimento ou decrescimento.')

# 3. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
print('\n# 3. Vogal ou Consoante')
letra = input('Digite uma letra: ').lower()
vogais = 'aeiou'

if letra.isalpha() and len(letra) == 1:
    if letra in vogais:
        print('A letra é uma vogal.')
    else:
        print('A letra é uma consoante.')
else:
    print('Entrada inválida. Por favor, digite apenas uma letra.')

# 4. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
print('\n# 4. Maior e Menor Preço em 3 Anos')
preco_ano1 = float(input('Informe o preço médio do carro no primeiro ano: '))
preco_ano2 = float(input('Informe o preço médio do carro no segundo ano: '))
preco_ano3 = float(input('Informe o preço médio do carro no terceiro ano: '))

# Inicializa maior e menor com o primeiro preço
maior = preco_ano1
menor = preco_ano1

# Verifica o maior
if preco_ano2 > maior:
  maior = preco_ano2
if preco_ano3 > maior:
  maior = preco_ano3

# Verifica o menor
if preco_ano2 < menor:
  menor = preco_ano2
if preco_ano3 < menor:
  menor = preco_ano3

print(f'O preço mais alto foi de R$ {maior:.2f}.')
print(f'O preço mais baixo foi de R$ {menor:.2f}.')

# 5. Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
print('\n# 5. Produto mais barato')
p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

if p1 < p2 and p1 < p3:
    print('O primeiro produto (R$ %.2f) é o mais barato.' % p1)
elif p2 < p1 and p2 < p3:
    print('O segundo produto (R$ %.2f) é o mais barato.' % p2)
elif p3 < p1 and p3 < p2:
    print('O terceiro produto (R$ %.2f) é o mais barato.' % p3)
elif p1 == p2 == p3:
    print('Os produtos possuem o mesmo preço (R$ %.2f).' % p1)
else:
    # Caso haja empate entre dois produtos
    min_price = min(p1, p2, p3)
    produtos_mais_baratos = []
    if p1 == min_price:
        produtos_mais_baratos.append('primeiro')
    if p2 == min_price:
        produtos_mais_baratos.append('segundo')
    if p3 == min_price:
        produtos_mais_baratos.append('terceiro')
    print(f"Os produtos mais baratos (R$ {min_price:.2f}) são: {' e '.join(produtos_mais_baratos)}.")

# 6. Escreva um programa que leia três números e os exiba em ordem decrescente.
print('\n# 6. Ordenação Decrescente de 3 Números')
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

print('Ordem decrescente:')

# Lógica de comparação para ordenação
if (num1 >= num2) and (num1 >= num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else: # num3 é o maior
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

# 7. Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
print('\n# 7. Saudação por Turno')
turno = input('Digite em qual turno você estuda (manhã, tarde ou noite): ').lower()

if turno == 'manhã':
  print('Bom Dia!')
elif turno == 'tarde':
  print('Boa Tarde!')
elif turno == 'noite':
  print('Boa Noite!')
else:
  print('Valor Inválido!')


# 8. Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
print('\n# 8. Par ou Ímpar')
try:
    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')
except ValueError:
    print('Entrada inválida. Por favor, digite um número inteiro.')


# 9. Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
print('\n# 9. Inteiro ou Decimal')
try:
    num = float(input('Digite um número: '))

    if num % 1 == 0:
        print('O número é inteiro.')
    else:
        print('O número é decimal.')
except ValueError:
    print('Entrada inválida. Por favor, digite um número.')

# Momento dos projetos

# 10. Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. 
# O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
print('\n# 10. Calculadora Detalhada')
try:
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))
    operacao = input('Informe a operação desejada (+, -, *, /): ')

    resultado = None

    # 1. Executa a operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print('Erro: Divisão por zero não é permitida.')
            resultado = 0
    else:
        print('Operação inválida.')
        resultado = 0

    if resultado is not None:
        print(f'Resultado: {resultado}')

        # 2. Verifica se é inteiro ou decimal
        if resultado % 1 == 0:
            print('O resultado é inteiro.')
            # A verificação de par/ímpar só faz sentido para números inteiros
            # 3. Verifica se é par ou ímpar (só para inteiros)
            if resultado % 2 == 0:
                print('O resultado é par.')
            else:
                print('O resultado é ímpar.')
        else:
            print('O resultado é decimal.')

        # 4. Verifica se é positivo, negativo ou neutro
        if resultado > 0:
            print('O resultado é positivo.')
        elif resultado == 0:
            print('O resultado é neutro.')
        else:
            print('O resultado é negativo.')

except ValueError:
    print('Entrada inválida. Por favor, digite números válidos.')

# 11. Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. 
# O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno.
print('\n# 11. Classificação de Triângulos')
try:
    print('Coletaremos os lados de um triângulo.')
    lado1 = float(input('Digite o comprimento do primeiro lado: '))
    lado2 = float(input('Digite o comprimento do segundo lado: '))
    lado3 = float(input('Digite o comprimento do terceiro lado: '))

    # 1. Verifica se os lados formam um triângulo
    if (lado1 > 0 and lado2 > 0 and lado3 > 0) and \
       (lado1 + lado2 > lado3) and \
       (lado2 + lado3 > lado1) and \
       (lado1 + lado3 > lado2):
        print('Os valores podem formar um triângulo!')

        # 2. Classifica o tipo de triângulo
        if (lado1 == lado2) and (lado2 == lado3):
            print('O triângulo é equilátero (três lados iguais).')
        elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
            print('O triângulo é escaleno (três lados diferentes).')
        else:
            print('O triângulo é isósceles (dois lados iguais).')
    else:
        print('Os valores não podem formar um triângulo! (A soma de quaisquer dois lados deve ser maior que o terceiro, e todos os lados devem ser positivos).')

except ValueError:
    print('Entrada inválida. Por favor, digite números para os comprimentos dos lados.')

# 12. Cálculo de valor a ser pago por combustível com desconto
print('\n# 12. Cálculo de Combustível com Desconto')

PRECO_ETANOL = 1.70
PRECO_DIESEL = 2.00

try:
    quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
    tipo_combustivel = input('Informe o tipo de combustível (E para etanol e D para diesel): ').upper()

    preco_litro = 0
    desconto = 0

    if tipo_combustivel == 'E':
        preco_litro = PRECO_ETANOL
        if quantidade_litros <= 15:
            desconto = 0.02  # 2%
        else:
            desconto = 0.04  # 4%
    elif tipo_combustivel == 'D':
        preco_litro = PRECO_DIESEL
        if quantidade_litros <= 15:
            desconto = 0.03  # 3%
        else:
            desconto = 0.05  # 5%
    else:
        print('Tipo de combustível inválido!')
        # Preço e desconto permanecem 0
    
    if preco_litro > 0:
        # Cálculo do valor
        valor_total_sem_desconto = preco_litro * quantidade_litros
        valor_desconto = valor_total_sem_desconto * desconto
        valor_pago = valor_total_sem_desconto - valor_desconto

        print(f'Preço por litro: R$ {preco_litro:.2f}')
        print(f'Desconto aplicado: {desconto*100:.0f}%')
        print(f'Valor do desconto: R$ {valor_desconto:.2f}')
        print(f'Valor a ser pago pelo cliente: R$ {valor_pago:.2f}')

except ValueError:
    print('Entrada inválida. Por favor, digite um número para a quantidade de litros.')

# 13. Análise de variação de vendas anuais
print('\n# 13. Análise de Variação de Vendas')
try:
    venda_2022 = float(input('Informe a quantidade de vendas em 2022: '))
    venda_2023 = float(input('Informe a quantidade de vendas em 2023: '))

    if venda_2022 > 0:
        # Cálculo da variação percentual: 100 * (Venda_2023 - Venda_2022) / Venda_2022
        var_percentual = 100 * (venda_2023 - venda_2022) / venda_2022
        print(f'Variação percentual: {var_percentual:.2f}%')

        # Análise condicional
        if var_percentual > 20:
            print('Sugestão: Bonificação para o time de vendas.')
        elif var_percentual >= 2: # Entre 2% e 20% (inclusive 2 e 20)
            print('Sugestão: Pequena bonificação para time de vendas.')
        elif var_percentual >= -10: # Entre 2% e -10% (exclusive 2, inclusive -10)
            print('Sugestão: Planejamento de políticas de incentivo às vendas.')
        else: # Abaixo de -10%
            print('Sugestão: Corte de gastos.')
    elif venda_2022 == 0:
        if venda_2023 > 0:
            print('Variação percentual: Crescimento infinito (de 0 para > 0). Sugestão: Bonificação para o time de vendas.')
        else:
            print('Variação percentual: 0%. Sugestão: Planejamento de políticas de incentivo às vendas.')
    else:
        print('Vendas em 2022 não podem ser negativas.')

except ValueError:
    print('Entrada inválida. Por favor, digite números para as vendas.')

print('\nFim das atividades de condicionais!')