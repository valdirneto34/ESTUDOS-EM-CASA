''' Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).strip().title()
nome = nome.split()
print('Muito prazer em te conhecer {}!'.format(nome[0]))
print('Seu primeiro nome é: {}.'.format(nome[0]))
print('Seu último nome é: {}.'.format(nome[len(nome)-1]))
