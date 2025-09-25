'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''


maior = homens = mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo in 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de {maior} pessoas com mais de 18 anos.')
print(f'Total de {homens} homens cadastrados.')
print(f'Total de {mulheres} mulheres com menos de 20 anos.')
