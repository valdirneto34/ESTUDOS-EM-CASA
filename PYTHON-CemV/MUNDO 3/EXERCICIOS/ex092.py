'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
anoatual = datetime.now().year

pessoa = {}
print('=-'*30)
pessoa['Nome'] = str(input("Nome: ")).capitalize()
nasc = int(input("Ano de Nascimento: "))
pessoa['Idade'] = anoatual - nasc
pessoa['CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))
if pessoa['CTPS'] != 0:
    pessoa['Contratacao'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = float(input("Salário: R$"))
    pessoa['Aposentadoria'] = pessoa['Idade'] + 35 - (anoatual - pessoa['Contratacao'])
print('=-'*30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}.')
print('=-'*30)
