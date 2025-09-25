

from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 15)
computador = randint(0, 11)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    soma = computador + jogador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if opcao == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR!')
            print('Você GANHOU!')
            cont += 1
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu ÍMPAR!')
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu ÍMPAR!')
            print('Você GANHOU!')
            cont += 1
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR!')
            print('Você PERDEU!')
            break
    print('=-' * 15)
    print('Vamos novamente...')
print(f'Você ganhou {cont} vezes consecutivas!')
