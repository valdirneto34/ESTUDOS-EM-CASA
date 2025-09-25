import os

pasta = os.path.dirname(__file__)

nome = "teste.txt"
f = open(pasta+"\\"+nome, "at")
# r - read - LEITURA
# a -  append - ANEXAR
# w - write - ESCRITA
# x - create - CRIAR
# t - text - TEXTO
# b - binary - BINÁRIO

txt = input("Digite um texto: ")
f.write(f'{txt}\n')


f.close()
