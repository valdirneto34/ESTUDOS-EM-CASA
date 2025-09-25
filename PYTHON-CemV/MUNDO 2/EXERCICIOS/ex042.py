'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso 
de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triângulo!')
    if a == b and b == c:
        print('Formará um triângulo equilátero, pois todos os lados são iguais. ')
    elif a != b and b != c and a != c:
        print('Formará um triângulo escaleno, pois todos os lados são diferentes.')
    else:
        print('Formará um triângulo isóceles, pois tem dois lados iguais.')
else:
    print('Elas não podem formar um triângulo!')
