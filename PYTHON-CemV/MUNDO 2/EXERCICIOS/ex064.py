'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


print('-='*24)
print('Vamos ver a soma entre vários números inteiros.')
print('Se quiser parar, digite 999.')
print('-=' * 24)
n = 0
q = 0
t = 0
n = int(input('Digite um número inteiro: '))
while n != 999:
    n = int(input('Digite um número inteiro: '))
    t += n
    q += 1
print('Programa encerrado!')
print('Foram digitados {} números e a soma entre eles é de {}.'.format(q, t))
