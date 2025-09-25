'''Refaça o DESAFIO 009, mostrando a tabuada de um número que
 o usuário escolher, só que agora utilizando um laço for.'''

print('Vamos descobrir a tabuada de um número!')
num = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range(1, 11):
    print('{} x {:2} = {}'.format(num, tabuada, num*tabuada))
print('FIM!')
