# LAÇO C NO INTERVALO():
for c in range(1, 7):
    print('Oi')
print('FIM')
for c in range(6, 0, -1): #-1 para saber que tem que subtrair
    print(c)
print('FIM')
for c in range(0, 6): #o programa ignora o último número
    print(c)
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os números foi {}.'.format(s))
