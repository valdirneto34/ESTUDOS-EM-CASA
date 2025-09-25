#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa
# a²=b²+c²

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
#ou hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa dos catetos {} e {} vale {:.2f}.'.format(co, ca, hi))
