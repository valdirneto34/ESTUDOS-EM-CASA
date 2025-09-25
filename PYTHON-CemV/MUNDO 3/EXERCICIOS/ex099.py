'''Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep

def maior (*inteiros):
    print('-='*30)
    print('Analizando os valores passados...')
    cont = mai = 0
    for num in inteiros:
        print(f'{num} ', end='', flush=True)
        if cont == 0:
            mai = num
        elif num > mai:
            mai = num
        sleep(0.3)
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')

#PP
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('-='*30)
