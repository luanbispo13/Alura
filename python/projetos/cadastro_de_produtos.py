import os

produtos = [{'nome': 'camiseta', 'categoria': 'esporte', 'status': False},
            {'nome': 'meia', 'categoria': 'esporte', 'status': True}]

def exibir_nome_do_programa():
    print('loja do Luan\n')

def exibir_opcoes():
    print('1. cadastrar produto')
    print('2. listar produto')
    print('3. alterar status do produto')
    print('4. sair\n')

def finalizar_app():
    exibir_subtitulo('encerrando o aplicstatus')

def voltar_ao_menu_principal():
    input('aperte a tecla Enter para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_novo_produto():
    exibir_subtitulo('cadastro de novos produtos')
    nome_do_produto = input('digite o nome do produto que deseja cadastrar: ')
    categoria = input('digite a categoria do produto {}: '.format(nome_do_produto))
    dados_do_restaurante = {'nome': nome_do_produto, 'categoria': categoria, 'status': False}
    produtos.append(dados_do_restaurante)
    print('o produto {} foi cadastrado com sucesso!\n'.format(nome_do_produto))
    voltar_ao_menu_principal()

def listar_produtos():
    exibir_subtitulo('listando os produtos')

    print(f'{'produto'.ljust(20)} {'categoria'.ljust(20)} status')
    for produto in produtos:
        nome_produto = produto['nome']
        categoria = produto['categoria']
        status = 'ativado' if produto['status'] else 'desativado'
        print(f'{nome_produto.ljust(20)} {categoria.ljust(20)} {status}')
        
    voltar_ao_menu_principal()

def alternar_status_produto():
    exibir_subtitulo('alterando status do produto')
    nome_produto = input('digite o nome do produto que deseja alterar o status: ')
    produto_encontrado = False

    for produto in produtos:
        if nome_produto == produto['nome']:
            produto_encontrado = True
            produto[''] = not produto['status']
            mensagem = 'o produto {} foi ativado com sucesso'.format(nome_produto) if produto['status'] else 'o produto {} foi desativado com sucesso'.format(nome_produto)
            print(mensagem)

    if not produto_encontrado:
        print('o produto não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_produto()

        elif opcao_escolhida == 2:
            listar_produtos()

        elif opcao_escolhida == 3:
            alternar_status_produto()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()