'''Crie um programa que leia nome e duas notas 
de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e 
permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2.0
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 24)
for i, aluno in enumerate(lista):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-' * 26)
while True:
    print('-' * 40)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}.')
    print('-' * 20)
print('<<< VOLTE SEMPRE >>>')
