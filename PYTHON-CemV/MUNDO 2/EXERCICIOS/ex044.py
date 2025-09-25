''' Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''

preco = float(input('Digite o preço do produto:R$ '))
print('Digite 1 se a forma de pagamento for À VISTA NO DINHEIRO OU CHEQUE.')
print('Digite 2 se a forma de pagamento for À VISTA NO CARTÃO.')
print('Digite 3 se a forma de pagamento for EM ATÉ 2x NO CARTÃO.')
print('Digite 4 se a forma de pagamento for EM 3x OU MAIS NO CARTÃO.')
forma = int(input('Pode digitar: '))
if forma == 1:
    print('O preço será de R${:.2f}'.format(preco-preco*0.10))
elif forma == 2:
    print('O preço será de R${:.2f}'.format(preco-preco*0.05))
elif forma == 3:
    print('O preço não será alterado, continuará sendo de R${:.2f}'.format(preco))
elif forma == 4:
    print('O preço será de R${:.2f}'.format(preco+preco*0.2))
    