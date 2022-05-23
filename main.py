pecas = []
# ---------------COMEÇO cadastrarPeça---------------
def cadastrarPeca(codigo): # Função de cadastro que recebe os ítens
    print('Você selecionou a opção de cadastrar peça!')
    print('Código da peça: {}'.format(codigo))
    nome = input('Por favor, entre com o NOME da peça: ')
    fabricante = input('Por favor, entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor, entre com o VALOR (R$) da peça: '))
    cadastroDicionario = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor' : valor} # Mostra a lista de
    # dicionários
    pecas.append(cadastroDicionario.copy()) # Adiciona um item no dicionário
    cadastroDicionario.clear() # Limpa um item do dicionário
# ---------------FIM cadastrarPeça---------------
# ---------------COMEÇO consultarPeça-----------
def consultarPeca():
    while True: # autenticação de resposta
        print('Você selecionou o opção de consultar peças')
        opConsultar = int(input('Escolha a opção desejada:\n1 - Consultar Todas as Peças\n2 - Consultar Peças por Código\n3'
                            '-Consultar Peças por Fabricante\n4- Retornar\n>> '))
        if opConsultar == 1:
                print('--------------------')
                for registro in pecas:
                    for key, value in registro.items(): # Seleciona cada conjunto chave : valor do dicionário
                        print('{} : {}' .format(key, value))
                print('--------------------')
        elif opConsultar == 2:
                entrada = int(input('Digite o CÓDIGO da peça: '))
                print('--------------------')
                for registro in pecas:
                    if registro['codigo'] == entrada:
                        for key, value in registro.items():
                            print('{} : {}'.format(key, value))
                print('--------------------')
        elif opConsultar == 3:
                entrada = input('Digite o FABRICANTE da peça: ')
                print('--------------------')
                for registro in pecas:
                    if registro['fabricante'] == entrada:
                        for key, value in registro.items():
                            print('{} : {}'.format(key, value))
                print('--------------------')
        elif opConsultar == 4: # Retorna ao Menu
                    break
# ---------------FIM consultarPeça---------------
# ---------------COMEÇO removerPeça---------------
def removerPeca():
    print('Você selecionou remover Peça')
    entrada = int(input('Digite o código da peça a ser removida: '))
    for registro in pecas:
        if registro['codigo'] == entrada:
            pecas.remove(registro) # Remover peça do registro
# ---------------FIM removerPeça---------------
# ---------------COMEÇO MAIN---------------
print('Bem Vindo ao Controle de Estoque da Bicicletaria da Lívia')
registroPeca = 0 # iniciando a função com 0
while True:
    opcao = int(input('Escolha a opção desejada:\n1- Cadastrar Peças\n2- Consultar Peças\n3- Remover Peças\n4- '
               'Sair\n>> '))
    if opcao == 1:
        registroPeca = registroPeca + 1
        cadastrarPeca(registroPeca)
    elif opcao == 2:
        consultarPeca()
    elif opcao == 3:
        removerPeca()
    elif opcao == 4:
        print('Sair')
        break
    # ---------------FIM MAIN---------------




