'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

km = float(input('Qual a velocidade do carro em Km/h: '))
if km > 80:
    print('Você excedeu o limite e foi multado em R${:.2f}!'.format((km-80)*7))
else:
    print('Muito bem, você está no limite de 80Km/h!')
