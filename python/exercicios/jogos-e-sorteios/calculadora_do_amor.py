import random

def calculadora_do_amor(nome1, nome2):
    # Normaliza os nomes para minúsculas e remove espaços
    nome1 = nome1.lower().replace(" ", "")
    nome2 = nome2.lower().replace(" ", "")
    
    # Combina os nomes e calcula um "índice de amor" único
    nomes_combinados = nome1 + nome2
    random.seed(len(nomes_combinados))  # Define a semente para o gerador de números aleatórios
    indice_de_amor = random.randint(50, 100)  # Índice de amor entre 50% e 100%
    
    return indice_de_amor

# Obtém os nomes do usuário
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

# Calcula e exibe a porcentagem de compatibilidade
pontuacao = calculadora_do_amor(nome1, nome2)
print(f"A compatibilidade amorosa entre {nome1} e {nome2} é de {pontuacao}%!")