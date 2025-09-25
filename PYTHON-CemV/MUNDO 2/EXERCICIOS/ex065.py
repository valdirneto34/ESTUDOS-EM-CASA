''' Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores 
e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer 
ou não continuar a digitar valores.'''


print('-='*30)
print('Vamos ver a média, o maior e o menor dentre vários números.')
print('-='*30)
t = 0
r = 'S'
q = 0
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('Digite um número inteiro: '))
    t = t + n
    q = q + 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
media = t / q
print('Você digitou {} números e a média foi {}.'.format(q, media))
print('O maior é valor {} e o menor valor é {}.'.format(maior, menor))
