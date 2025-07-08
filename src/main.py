print('Bem-vindo a loja do Pedro Henrique')
valorunitário = float(input('Entre com o valor do produto '))
quantidade = int(input('Entre com a quantidade do produto: '))
'''
variáveis que tem seus valores associados a entrada da função input, criadas para receberem o valor do produto do cliente,
e a quantidade deste produto que o cliente deseja comprar.
'''

total = valorunitário * quantidade
'''
Variável que calcula o total a pagar pela quantidade do produto, que foi especificada anteriormente pelo cliente.
'''

if total < 2500:
    totaldesconto = total
    '''
    estrutura condicional que calcula o total do produto escolhido, com 0% de desconto aplicado.
    '''

elif total >= 2500 and total < 6000:
    totaldesconto = total * 4/100
    '''
    estrutura condicional que calcula o total do produto escolhido, com 4% de desconto aplicado.
    '''

elif total >= 6000 and total < 10000:
    totaldesconto = total * 7/100
    '''
    estrutura condicional que calcula o total do produto escolhido, com 7% de desconto aplicado.
    '''

elif total >= 10000:
    totaldesconto = total * 11/100
    '''
    estrutura condicional que calcula o total do produto escolhido, com 11% de desconto aplicado.
    '''

print(f'O valor SEM desconto: {total}')
'''
função print criada para mostrar ao usuário, o valor total de sua compra, sem desconto.
'''

if total == totaldesconto:
    print(f'O valor COM desconto: {total}')
else: print(f'O valor COM desconto: {total - totaldesconto}')
'''
Estrutura de decisão, criada com o objetivo de impedir que, na circunstância onde a variável (total) for igual a variável 
(totaldesconto), ou seja, quando o desconto aplicado for 0%, o valor apresentado não seja 0, e sim o valor original, e 
para mostrar ao cliente o seu total com desconto diferente de 0%.
'''
