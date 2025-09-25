'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

jogos = []
lista = []
num = 0
print('-' * 40)
print('{:^40}'.format('JOGA NA MEGA-SENA'))
print('-' * 40)
qtd = int(input('Digite quantos jogos você quer fazer: '))
for c in range(0, qtd):
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    jogos.append(lista[:])
    lista.clear()
print(f'{'-=' * 4} SORTEANDO {qtd} JOGOS {'-=' * 4}')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'{'-=' * 5} < BOA SORTE! > {'-=' * 5}')
