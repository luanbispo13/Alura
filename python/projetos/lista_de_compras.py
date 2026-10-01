# Crie um programa que permite ao usuário adicionar itens a uma lista de compras.

listas_compras = []

while True:
    item = input("digite um item para adicionar a lista de compras (ou 'sair' para terminar): ")
    if item.lower() == 'sair':
        break
    else:
        listas_compras.append(item)

print("listas de compras:")
for item in listas_compras:
    print("-", item)