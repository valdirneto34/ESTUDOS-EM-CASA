'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)

pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM!')
