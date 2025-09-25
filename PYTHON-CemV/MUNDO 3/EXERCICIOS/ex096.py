''' Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''


def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area} m².')


#Programa Principal
print("CONTROLE DE TERRENOS".center(40))
print('-'*40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
