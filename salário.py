# crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salário = float(input('qual salário do funcionário? '))
novo = salário + (salário * 15/100)

print('o funcionário que ganhava R${:.2f} \npassa a receber R${:.2f}'.format(salário, novo))