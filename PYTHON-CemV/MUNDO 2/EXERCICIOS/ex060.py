'''Faça um programa que leia um 
número qualquer e mostre o seu fatorial.'''

from math import factorial
r = 'S'
while r == 'S':
    n = int(input('Digite um número para vermos o seu fatorial: '))
    f = factorial(n)
    print('O fatorial de {} é {}.'.format(n, f))
    r = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
print('Programa encerrado!')
