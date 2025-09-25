''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))

print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
c = max(lista)
for n, v in enumerate(lista):
    if v == c:
        print(f'{n}...', end='')
m = min(lista)
print(f'\nO menor valor digitado foi {m} nas posiçõoes ', end='')
for n, v in enumerate(lista):
    if v == m:
        print(f'{n}...', end='')
