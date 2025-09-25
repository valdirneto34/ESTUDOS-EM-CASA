#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do sen, cos e tg desse ângulo.

from math import sin, cos, tan, radians
ang=float(input('Digite o a medida do ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Dado o ângulo de {}°, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(ang, sen, cos, tan))
