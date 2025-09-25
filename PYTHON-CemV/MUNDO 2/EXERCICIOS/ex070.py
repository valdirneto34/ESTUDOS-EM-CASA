''' Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print('-' * 40)
print('{:-^40}'.format('LOJAS MORFEUS'))
print('-' * 40)
total = 0
maismil = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        maismil += 1
    if cont == 1:
        maisbarato = preco
        barato = nome
    elif preco < maisbarato:
        maisbarato = preco
        barato = nome
    r = ' '
    while r not in 'SN':
        r = str(input('Vai querer continuar: [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto foi de R${total:.2f}')
print(f'Temos {maismil} produtos que custam mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${maisbarato:.2f}.')
