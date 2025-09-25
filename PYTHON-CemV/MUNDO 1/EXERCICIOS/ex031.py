'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

print('Vamos calcular o valor de uma passagem!')
d = float(input('Digite a distância da viagem em Km: '))
if d <= 200:
    print('O valor da passagem será de R${:.2f}!'.format(d*0.5))
else:
    print('O valor da passagem será de R${:.2f}!'.format(d*0.45))
