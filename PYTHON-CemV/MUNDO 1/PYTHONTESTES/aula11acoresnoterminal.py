'''\033[0;33;44m
print('\033[0;33;44m')'''
'''   TESTES   '''
nome = str(input('Qual o seu nome? ')).upper().strip()
print('\033[0;30;41m{}\033[m'.format(nome))
print('\033[4;33;44m{}\033[m'.format(nome))
print('\033[1;35;43m{}\033[m'.format(nome))
print('\033[0;30;42m{}\033[m'.format(nome))
print('\033[0;0;0m{}\033[m'.format(nome))
print('\033[0;7;30m{}\033[m'.format(nome))
'''   TESTES   '''
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[0;97;40mOlá, Mundo!\033[m')
print('\033[0;30;107mOlá, Mundo!\033[m')
print('Olá, muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
