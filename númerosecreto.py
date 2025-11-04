# Crie um simples jogo em que o computador gera um número aleatório e o jogador tenta adivinhar.

import random

# Gera um número aleatório entre 1 e 100.
numero_secreto = random.randint(1, 100)

# Loop principal do jogo que continua até que o jogador adivinhe o número secreto.
while True:
    # Solicita ao jogador que insira um número.
    chute = int(input("Digite um número: "))
    
    # Verifica se o número inserido pelo jogador é igual ao número secreto.
    if chute == numero_secreto:
        print("Parabéns você acertou!")  # Avisa o jogador que ele acertou.
        break  # Encerra o jogo.
    # Caso o número inserido seja menor que o número secreto.
    elif chute < numero_secreto:
        print("Tente um número maior.")  # Informa ao jogador para tentar um número maior.
    # Caso o número inserido seja maior que o número secreto.
    else:
        print("Tente um número menor.")  # Informa ao jogador para tentar um número menor.
