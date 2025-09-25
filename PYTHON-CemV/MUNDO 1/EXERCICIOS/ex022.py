'''# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. -
 Quantas letras ao todo sem considerar espaços.- Quantas letras tem o primeiro nome.'''

'''Valdir de Souza Carvalho Neto'''

nome= str(input('Digite o seu nome completo: ')).strip()
print ('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print ('Seu nome em minúsculo é {}.'.format(nome.lower()))
print ('Seu nome ao todo tem {} letras.'.format(len(nome)-nome.count(' ')))
dividido = (nome.split())
print ('Seu primeiro nome é: {}, e ele tem {} letras.'.format(dividido[0], len(dividido[0])))
