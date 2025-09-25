'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

from urllib import request, error

try:
    site = request.urlopen("https://www.youtube.com.br")
except error.URLError:
    print(f'\033[1;31mO site Youtube não está acessível no momento.\033[m')
else:
    print(f'\033[1;34mConsegui acessar o site Youtube com sucesso!\033[m')
    # print(site.read())
