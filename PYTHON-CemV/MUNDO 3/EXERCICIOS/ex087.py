'''Aprimore o desafio anterior, mostreando no final:
a)A soma de todos os valores pares digitados.
b)A soma dos valores da terceira coluna.
c)O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somacoluna3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        if(matriz[l][c] % 2 == 0):
            pares += matriz[l][c]
        if(c == 2):
            somacoluna3 += matriz[l][c]
        if(l == 1):
            if c == 0:
                maior = matriz[l][c]
            elif(matriz[l][c] > maior):
                maior = matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da 3ª coluna é {somacoluna3}.')
print(f'O maior valor da segunda linha é {maior}.')
print('-='*30)
