'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

s = int(input('Digite o valor do salário R$'))
if s > 1250:
    print('Com o acréscimo de R${:.2f}, o novo salário será de R${:.2f}!'.format((s*0.1),(s*1.1)))
else:
    print('Com o acréscimo de R${:.2f}, o novo salário será de R${:.2f}!'.format((s*0.15),(s*1.15)))
