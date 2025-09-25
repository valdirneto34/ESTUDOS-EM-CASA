'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou!')'''

n = s = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    s += n
# print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')

# F Strings
nome = 'Valdir'
idade = 19
salario = 1420.5
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome ,idade)) # PYTHON 3
print('O %s tem %d anos.' %(nome, idade)) # PYTHON 2
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}!')
