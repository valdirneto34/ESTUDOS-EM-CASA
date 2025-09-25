# Faça um algoritmo que leia o preço de um produto e mostre
# o novo preço com desconto de 5%

preco= float(input('Digite o preço do produto:R$'))
npreco= preco-(preco * (5/100))
print('O novo preço do produto será de R${:.2f}!'.format(npreco))