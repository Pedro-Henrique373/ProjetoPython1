def cadastrar_livro(id):
    print('---------------------------------------------')
    print('---------- MENU CADASTRAR LIVRO -------------')
    global id_global
    id_global += id
    dados = {'nome': [], 'autor': [], 'editora': []}
    print(f'Id do livro: {id_global}')
    dados['nome'] = input('Por favor entre com o nome do Livro: ')
    dados['autor'] = input('Por favor entre com o autor do Livro: ')
    dados['editora'] = input('Por favor entre com a editora do Livro ')
    print('---------------------------------------------')
    dado1 = dados['nome']
    dado2 = dados['autor']
    dado3 = dados['editora']
    lista_livro.append([id_global, dado1, dado2, dado3])
    print()
    return id_global
'''
função criado com o objetivo de possibilitar e armazenar os cadastros de livros dos usuários, através das funções, print, input 
e append, além de utilização de métodos de listas.
'''


def consultar_livro():
    cont = 0
    while True:
        print('--------------------------------------------')
        print('---------- MENU CONSULTAR LIVRO ------------')
        print('Escolha a opção desejada: ')
        print('1 - Consultar todos os Livros ')
        print('2 - Consultar Livros por Id ')
        print('3 - Consultar Livro(s) por autor')
        print('4 - Retomar')
        consultar = int(input('>>'))
        print()
        if consultar == 1:
            for cadastros in (0, len(lista_livro), 1):
                cont += 1
                if cont == len(lista_livro):
                    break
                print(f'id: {lista_livro[cont][0]}')
                print(f'nome: {lista_livro[cont][1]}')
                print(f'autor: {lista_livro[cont][2]}')
                print(f'editora: {lista_livro[cont][3]}')
                print()
                continue

        elif consultar == 2:
            id_global = int(input('digite o id do seu livro:'))
            print()
            print(f'id: {lista_livro[id_global][0]}')
            print(f'nome: {lista_livro[id_global][1]}')
            print(f'autor: {lista_livro[id_global][2]}')
            print(f'editora: {lista_livro[id_global][3]}')
            print()
            continue

        elif consultar == 3:
            cont1 = 0
            print()
            autor = input('Digite o autor do(S) livro(s):')
            print()
            for cadastros in lista_livro:
                cont1 += 1
                if cont1 - 1 == len(lista_livro):
                    break
                else:
                    for dados in cadastros:
                        if dados == autor:
                            print('----------------')
                            print(f'id: {lista_livro[cont1 - 1][0]}')
                            print(f'nome: {lista_livro[cont1 - 1][1]}')
                            print(f'autor: {lista_livro[cont1 - 1][2]}')
                            print(f'editora: {lista_livro[cont1 - 1][3]}')
                            print('----------------')
                            print()
                            break
            continue

        elif consultar == 4:
            print('Retornando ao menu principal...')
            print()
            break

        else:
            print('opção invalida')
            print()
'''
função criada com o objetivo de possibilitar aos usuários da livraria, consultar seus livros cadastrados, sejam todos eles, 
ou algum em especifíco, seja por inserção do id do livro em questão, seja pelo autor, possibilitada por uma implementação
de estruturas de seleção, e manipulação de estruturas de dados.
'''


def remover_livro():
    while True:
        print('--------------------------------------------')
        print('------------ MENU REMOVER LIVRO ------------')
        id_global = int(input('Digite o id do livro a ser removido: '))
        if id_global == len(lista_livro) - 1 or id_global < len(lista_livro):
            del lista_livro[id_global]
            print('Livro removido com sucesso!')
            print('--------------------------------------------')
            print()
            return lista_livro

        elif ValueError:
            print('Id inválido\n')
'''
função criada com o objetivo de fornecer ao usuário, a possibilidade de remoção dos seus livros que foram cadastrados, através 
da inserção dos livros em questão, por meio de uma estrutura de decisão implementada, e correção de exceção.
'''


print('Bem vindo a Livraria do Pedro Henrique')
lista_livro = ['inicio']
id_global = 0
id = 1
while True:
    print('---------------------------------------------')
    print('-------------- MENU PRINCIPAL ---------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livros')
    print('2 - Consultar Livros')
    print('3 - Remover Livros')
    print('4 - Encerrar programa')
    cont = 0
    escolha = int(input('>>'))
    if escolha == 1:
        print()
        cadastrar_livro(id)
        continue

    elif escolha == 2:
        print()
        consultar_livro()

    elif escolha == 3:
        print()
        remover_livro()

    elif escolha == 4:
        print('Encerrando Programa... \n')
        break
        print()

    else:
        print('Opção inválida\n')
        continue
'''
algumas variáveis e uma estrutura de dados, inseridas antes do funcionamento do programa, com o intuito de garantir o correto 
funcionamento de todas as funções do programa, que são o cadastro, consulta e remoção, e além disso, uma estrutura de repetição, 
com o objetivo de criar um menu de visualização imediato, para qualquer um que executar o programa, e também, estruturas de 
decisões para fornecer aos usuários da livraria possibilidades de escolhas. 
'''
