'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e 
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep

nums = []

def sorteia(nums):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        nums.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
        
def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}!')

print('-='*30)
sorteia(nums)
somaPar(nums)
print('-='*30)
