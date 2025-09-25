'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        teclado = int(input('Digite um número entre 0 e 20: '))
        if 0 <= teclado <= 20:
            break
        print('Tente novamnente. ', end='')
    print(f'Você digitou o número {cont[teclado]}.')
    r = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('Programa Encerrado. Volte Sempre!')
