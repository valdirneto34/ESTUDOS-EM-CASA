# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km foram percoridos: '))
d = float(input('Quantos dias ele foi alugado: '))
total = (km * 0.15) + (d * 60)
print('Sabendo que o carro percorreu {:.2f} km, ficou {:.0f} dias alugado, o total a ser pago será de R${:.2f}!'.format(km, d, total))
