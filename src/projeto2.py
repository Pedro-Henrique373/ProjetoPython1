print('Bem vindo a Loja de Gelados do Pedro Henrique')
print('------------------Cardápio-------------------')
print('---------------------------------------------')
print('---| tamanho | Cupuaçu (CP) | Açai (AC) |----')
print('---|    P    |  R$  9,00    | R$ 11,00  |----')
print('---|    M    |  R$ 14,00    | R$ 16,00  |----')
print('---|    G    |  R$ 18,00    | R$ 20,00  |----')
print('---------------------------------------------')
acum = 0
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor == 'Cupuaçu':
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'p':
            valor = 9

        elif tamanho == 'm':
            valor = 14

        elif tamanho == 'g':
            valor = 18

        else:
            print('Tamanho invalido. Tente novamente')
            print()
            valor = 0
            continue
        acum += valor

    elif sabor == 'Açai':
        tamanho = input('Entre com o tamanho desejado (P/M/G)')
        if tamanho == 'p':
            valor = 11

        elif tamanho == 'm':
            valor = 16

        elif tamanho == 'g':
            valor = 20

        else:
            print('Tamanho invalido. Tente novamente')
            print()
            valor = 0
            continue
        acum += valor

    else:
        print('Sabor inválido. Tente novamente')
        print()
        continue
    '''
    uma estrutura de repetição while infinita, com uma estrutura de decisão aninhada, criada com o intuito de dar ao
    cliente, a possibilidade de escolher livremente dentre os sabores disponíveis, com seus tamanhos específicos, e seus 
    respectivos valores, quantas vezes quiser, e quantidade que quiser. 
    '''

    compra = print(f'Você pediu um {sabor} no tamanho {tamanho}: R${valor},00\n')
    '''
    variável criada para mostrar ao cliente, o valor do gelado que pediu, além de seu sabor e tamanho, através de uma função 
    print, e composição de strings.
    '''

    decisão = input('Deseja mais alguma coisa? (S/N): ')
    print()
    '''
    variável na qual foi feita, por meio de uma função print, para perguntar ao cliente, se deseja continuar a comprar, ou 
    se deseja saber seu valor total.
    '''

    if decisão == 'n':
        print(f'O valor total a ser pago: R${acum},00')
        break

    elif decisão == 's':
        continue
    '''
    estruturas de seleção, criadas com o objetivo de mostrar ao cliente o valor total da sua compra, e se, caso o cliente
    desejar comprar mais gelados, retorna-ló novamente a seleção de produtos.
    '''

