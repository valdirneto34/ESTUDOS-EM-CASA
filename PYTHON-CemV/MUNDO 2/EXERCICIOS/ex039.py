'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade,se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Ainda vai se alistar em {} anos.'.format(saldo))
    ano = atual + saldo
    print('O alistamento será em {}.'.format(ano))
elif idade == 18:
    print('Já é hora de se alistar.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Já passou {} anos do alistamento.'.format(saldo))
    print('O alistamento foi em {}.'.format(ano))
