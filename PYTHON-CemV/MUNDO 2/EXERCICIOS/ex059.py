'''Exercício Python 059: Crie um programa que leia dois
 valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
print('=-='*15)
menu = 0
while True:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    menu = int(input('>>>>> Digite sua opção: '))
    if menu == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}.'.format(v1, v2, soma))
    elif menu == 2:
        produto = v1 * v2
        print('O produto dos fatores {} e {} é {}.'.format(v1, v2, produto))
    elif menu == 3:
        if v1 == v2:
            print('Os números {} e {} são iguais.'.format(v1, v2))
        elif v1 > v2:
            maior = v1
            print('O número {} é maior que {}.'.format(v1, v2))
        else:
            maior = v2
            print('O número {} é maior que {}.'.format(v2, v1))
    elif menu == 4:
        print('Informe os novos números:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundoo valor: '))
    elif menu == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida. Tente novamente!')
    print('=-='*15)
    sleep(0.5)
sleep(2)
print('Programa encerrado! Volte quando quiser!')
