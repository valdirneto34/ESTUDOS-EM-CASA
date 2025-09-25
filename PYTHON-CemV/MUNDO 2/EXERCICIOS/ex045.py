# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('\033[35;46mOLÁ, VAMOS JOGAR JOKENPÔ!!!\033[m')
print('''\033[35;46mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('\033[1;37;47mDigite sua escolha:\033[m '))
print('\033[36;40mJO\033[m')
sleep(1)
print('\033[36;40mKEN\033[m')
sleep(1)
print('\033[36;40mPÔ!!!\033[m')
print('\033[7;35;43m-=\033[m' * 12)              
print('\033[35;43mComputador jogou {}.\033[m'.format(itens[computador]))
print('\033[35;43mJogador jogou {}.\033[m'.format(itens[jogador]))
print('\033[7;35;43m-=\033[m' * 12)
if computador == 0: #comptador jogou PEDRA
    if jogador == 0:
        print('\033[97;47mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[4;32;43mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[4;31;43mCOMPUTADOR VENCE!\033[33m')
    else:
        print('\033[97;41mJOGADA INVÁLIDA!\033[m')
elif computador == 1: #comptador jogou PAPEL
    if jogador == 0:
        print('\033[4;31;43mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[97;47mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[4;32;43mJOGADOR VENCE!\033[m')
    else:
        print('\033[97;41mJOGADA INVÁLIDA!\033[m')
elif computador == 2: #comptador jogou TESOURA
    if jogador == 0:
        print('\033[4;32;43mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[4;31;43mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[97;47mEMPATE!\033[m')
    else:
        print('\033[97;41mJOGADA INVÁLIDA!\033[m')
