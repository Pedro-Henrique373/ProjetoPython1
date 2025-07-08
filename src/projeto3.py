def escolha_servico():
    while True:
        tipo = input('>>')
        if tipo == 'DIG':
            valorunitario = 1.10

        elif tipo == 'ICO':
            valorunitario = 1.0

        elif tipo == 'IPB':
            valorunitario = 0.40

        elif tipo == 'FOT':
            valorunitario = 0.20

        else:
            print('Escolha inválida, entre com o tipo do serviço novamente.')
            print()
            continue
        return valorunitario

'''
função que permite o cliente de escolher dentre os serviços disponíveis, através de uma implementação de um laço de 
repetição while infinito, com uma estrutura de condição aninhada.
'''


def num_pagina():
    while True:
        try:
            paginas = int(input('Entre com o número de páginas:'))
            if paginas < 20:
                desconto = 20
                diferenca = paginas
                return diferenca
                break

            elif paginas >= 20 and paginas < 200:
                desconto = (paginas * 15) // 100
                diferenca = paginas - desconto
                return diferenca
                break

            elif paginas >= 200 and paginas < 2000:
                desconto = (paginas * 20) // 100
                diferenca = paginas - desconto
                return diferenca
                break

            elif paginas >= 2000 and paginas < 20000:
                desconto = (paginas * 25) // 100
                diferenca = paginas - desconto
                return diferenca
                break

            elif paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                print()

        except:
            print('Valor não numérico')
            print()
'''         
função que faz com que o cliente possa escolher quantas páginas ele deseja que sejam copiadas do tipo de impressão que
ele anteriormente tinha selecionado, possibilitado por uma estrutura de repetição while infinita, e uma estrutura de seleção 
aninhada, além de correção de exceções.
'''


def servico_extra():
    while True:
        adicional = input('>> ')
        if adicional == '1':
            valor = 15.00
            return valor

        elif adicional == '2':
            valor = 40.00
            return valor

        elif adicional == '0':
            valor = 00.00
            return valor

        else:
            print('Serviço extra inválido. Tente novamente')
            print()
            continue
'''
função que permite que o cliente possa escolher entre os serviços extras disponibilizados pela copiadora.
'''

print()
print('Bem vindo a Copiadora do Pedro Henrique')
print()
print('Entre com o tipo de serviço desejado')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')
servico = escolha_servico()
num_pagina = num_pagina()
print('\nDeseja adicionar algum serviço?')
print('1 - Encadernação Simples - R$15,00')
print('2 - Encadernação Capa Dura - R$40,00')
print('0 - Não desejo mais nada')
extra = servico_extra()
total = (servico * num_pagina) + extra
print(f'\nTotal: R$ {total} (serviço: {servico} * páginas: {num_pagina} + extra: {extra})')
'''
funções print, onde umas garantem um layout para o cliente, e uma para mostrar para o usuário, seu total, qual serviço 
selecionou e outro extra, além da quantidade de páginas que determinou, e além disso, nomes de funções para invoca-lás, 
e fazer com que sejam executadas nos momentos apropriados, também uma variável, que tem como função, calcular o total que 
o cliente irá pagar. 
'''
