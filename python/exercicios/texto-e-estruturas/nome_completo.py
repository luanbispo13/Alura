nome = str(input('digite seu nome completo: ')).strip()
print('analisando o nome')
print('seu nome maíusculo é {}'.format(nome.upper()))
print('seu nome minúsculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))