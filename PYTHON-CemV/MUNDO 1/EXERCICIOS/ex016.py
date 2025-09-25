#Um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#EXEMPLO:Digite o número:6.127.
#O número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um valor: '))
pi=trunc(num)
print('O número {} tem como porção inteira {}.'.format(num, pi))
