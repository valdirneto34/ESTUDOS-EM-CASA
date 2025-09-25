''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é: {lista}.')
print(f'A lista de pares é: {pares}.')
print(f'A lista de  ímpares é: {impares}.')
