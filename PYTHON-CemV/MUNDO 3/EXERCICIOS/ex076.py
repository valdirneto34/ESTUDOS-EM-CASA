'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
list = ('Batata Extra', 4.99, 'Melancia', 1.99, 'Moranga Japonesa', 1.99, 'Mamão Formoso', 2.99, 'Couve de Folha', 2.99, 'Cebola Pirulito', 3.99, 'Cenoura Vermelha', 3.99, 'Batata Palito', 12.99, 'Coxa com Sobrecoxa', 5.99)
for posicao in range(0, len(list)):
    if posicao % 2 == 0:
        print(f'{list[posicao]:.<30}', end='')
    else:
        print(f'R${list[posicao]:>7.2f}')
print('-' * 40)
