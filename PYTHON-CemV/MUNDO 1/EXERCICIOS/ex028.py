'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
from time import sleep
n = random.randint(0, 5)
print('Vou pensar em um número entre 0 e 5.')
n2 = int(input('Tente adivinhar: '))
print('PROCESSANDO...')
sleep(2)
if n == n2:
    print('PARABÉNS! Você venceu! Temos pensamentos parecidos!')
else:
    print('Que pena, você perdeu!')
    print('Eu pensei no número {}, e não no {}.'.format(n, n2))
