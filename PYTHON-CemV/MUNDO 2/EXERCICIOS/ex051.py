'''Desenvolva um programa que leia o primeiro 
termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''


print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)

pt = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU!!')
