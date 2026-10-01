# crie um programa que gera os números primos até um determinado número

# Solicita ao usuário para digitar o limite até onde os números primos serão gerados
limite = int(input('digite o limite: '))

# Exibe uma mensagem indicando até onde os números primos serão gerados
print('números primos até', limite, ":")

# Loop para percorrer todos os números de 2 até o limite especificado
for num in range(2, limite + 1):
    
    # Assume que o número é primo até que se prove o contrário
    primo = True
    
    # Loop para verificar se o número é divisível por algum número entre 2 e num-1
    for i in range(2, num):
        if (num % i) == 0:  # Se o número for divisível, ele não é primo
            primo = False
            break  # Sai do loop assim que encontrar um divisor
    
    # Se o número não for divisível por nenhum número, ele é primo
    if primo:
        print(num)  # Imprime o número primo