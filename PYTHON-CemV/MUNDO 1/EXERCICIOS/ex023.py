''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''


num = int(input('Digite um número de 0 a 9999: '))
print ('Número digitado: {}.'.format(num))
print('Unidades: {}.\nDezenas: {}.'.format(num//1, num//10)) #só para entendimento
print('Centenas: {}.\nMilhares: {}.'.format(num//100, num//1000)) #só para entendimento
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Milhares: {}'.format(m))
print('Centenas: {}'.format(c))
print('Dezenas: {}'.format(d))
print('Unidades: {}'.format(u))
