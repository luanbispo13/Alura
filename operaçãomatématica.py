# Função para realizar operações matemáticas básicas entre dois números fornecidos pelo usuário.

# Ordem da Precedência: 1. [()] 2. [**] 3. [* / // %] e 4. [+ -]

# [+] adição, [-] subtração, [*] multiplicação, [/] divisão, [**] potência, [//] divisão inteira e [%] resto da divisão.

n1 = int(input('digite um valor: '))  # Recebe o primeiro número fornecido pelo usuário
n2 = int(input('digite outro valor: '))  # Recebe o segundo número fornecido pelo usuário

s = n1 + n2  # Realiza a adição entre os dois números
m = n1 * n2  # Realiza a multiplicação entre os dois números
d = n1 / n2  # Realiza a divisão entre os dois números
di = n1 // n2  # Realiza a divisão inteira entre os dois números
e = n1 ** n2  # Realiza a exponenciação, elevando o primeiro número à potência do segundo

# Exibe os resultados das operações para o usuário
print('a soma é {}, multiplicação é {} e a divisão é {}'.format(s, m, d))
print('divisão inteira é {} e a potência é {}'.format(di, e))