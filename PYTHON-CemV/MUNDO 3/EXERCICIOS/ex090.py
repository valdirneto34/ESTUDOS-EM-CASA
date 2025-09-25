'''Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
print('-='*30)
aluno['Nome'] = str(input("Nome do aluno: "))
aluno['Média'] = float(input(f"Média de {aluno["Nome"]}: "))
if aluno['Média'] >= 7:
    aluno['Situação'] = "Aprovado"
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = "Recuperação"
else:
    aluno['Situação'] = "Reprovado"
print('-='*30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
