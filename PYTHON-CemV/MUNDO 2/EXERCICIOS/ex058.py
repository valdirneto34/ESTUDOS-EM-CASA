'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

import random
computador = random.randint(0, 10)
palpites = 0
acertou = False
print('Sou seu computador... Vou pensar em um número entre 0 e 10.')
while not acertou:
    jogador = int(input('Tente adivinhar: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Parabéns, você acertou! Mas precisou de {} tentativas!'.format(palpites))
