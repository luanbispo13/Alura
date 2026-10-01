# Classe Cliente
import os
def limpar():
    os.system('cls')

class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        limpar()
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

# Classe Conta Bancária
class ContaBancaria:
    def __init__(self, cliente, numero_conta, saldo_inicial=0):
        limpar()
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):

        limpar()
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        limpar()
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")

# Classe Banco
class Banco:
    def __init__(self, nome_banco):
        limpar()
        self.nome_banco = nome_banco
        self.contas = []
        self.numero_conta = 1000  # Número de conta inicial

    def cadastrar_cliente(self):
        limpar()
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        email = input("E-mail do cliente: ")
        telefone = input("Telefone do cliente: ")

        novo_cliente = Cliente(nome, cpf, email, telefone)
        nova_conta = ContaBancaria(novo_cliente, self.numero_conta)
        self.contas.append(nova_conta)
        print(f"Conta {self.numero_conta} criada com sucesso para {nome}!")
        self.numero_conta += 1

    def buscar_conta(self, numero_conta):
        limpar()
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

    def operacoes(self):
        limpar()
        while True:
            print("\nMenu de Operações:")
            print("1. Cadastrar Cliente")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Consultar Saldo")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_cliente()

            elif opcao == '2':
                numero_conta = int(input("Número da conta: "))
                conta = self.buscar_conta(numero_conta)
                if conta:
                    valor = float(input("Valor do depósito: "))
                    conta.depositar(valor)
                else:
                    print("Conta não encontrada.")

            elif opcao == '3':
                numero_conta = int(input("Número da conta: "))
                conta = self.buscar_conta(numero_conta)
                if conta:
                    valor = float(input("Valor do saque: "))
                    conta.sacar(valor)
                else:
                    print("Conta não encontrada.")

            elif opcao == '4':
                numero_conta = int(input("Número da conta: "))
                conta = self.buscar_conta(numero_conta)
                if conta:
                    conta.consultar_saldo()
                else:
                    print("Conta não encontrada.")

            elif opcao == '5':
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    banco = Banco("Meu Banco")
    banco.operacoes()