'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

'''from time import sleep
print('=' * 26)
print('{:^26}'.format('BANCO MORFEU'))
print('=' * 26)
valor = int(input('Valor a ser sacado: R$ '))
print('=' * 26)
print('Analisando possibilidade de saque...')
sleep(2)
print('Contando cédulas...')
sleep(2)
total = valor
if valor < 1:
    print('Valor INVÁLIDO!')
cinquenta = valor // 50
valor -= 50 * cinquenta
vinte = valor // 20
valor -= 20 * vinte
dez = valor // 10
valor -= 10 * dez
um = valor // 1
print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('=' * 26)
print('Transacão realizada com sucesso!')
sleep(1)
print(f'Total de R${total} sacados!')
sleep(1)
print('Volte sempre ao BANCO MORFEU!')'''

from time import sleep
print('=' * 26)
print('{:^26}'.format('BANCO MORFEU'))
print('=' * 26)
valor = int(input('Que valor você quer sacar R$ '))
total = valor
ced = 100
totced = 0
print('Analisando possibilidade de saque...')
sleep(2)
print('Contando cédulas...')
sleep(2)
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
sleep(2)
print('=' * 30)
print('Volte sempre ao BANCO MORFEU!')
print('=' * 30)
