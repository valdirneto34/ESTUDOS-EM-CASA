'''Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

from time import sleep
soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
if cont <= 1:
    print('Vamos ver a soma do único número par que você digitou!')
else:
     print('Vamos ver a soma dos {} números pares que você digitou!'.format(cont))
sleep(1)
print('CALCULANDO!!!')
sleep(2)
print('\033[4;37;45mO total é: {}.\033[m'.format(soma))
