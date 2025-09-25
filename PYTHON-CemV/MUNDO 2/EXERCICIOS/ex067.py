'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''


while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    print('--' * 21)
    for c in range(1, 11):
        print(f'{t} x {c} = {t*c}')
    print('--' * 21)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')