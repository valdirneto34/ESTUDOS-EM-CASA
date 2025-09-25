import os
import sqlite3
from sqlite3 import Error


def ConexaoBanco():  # --------Conexão
    caminho = "C:\\PYTHON\\banco\\agenda"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()


def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro Por ID")
    print("5 - Consultar Registro Por Nome")
    print("6 - Sair")


def menuInserir():
    print()


def menuDeletar():
    print()


def menuAtualizar():
    print()


def menuConsultar():
    print()


def menuConsultarNomes():
    print()


opc = 0
while opc != 6:
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultar()
    elif opc == 5:
        menuConsultarNomes()
    elif opc == 6:
        os.system("cls")
        print("Programa Finalizado!")
        break
    else:
        os.system("cls")
        print("Opção inválida!")
        os.system("pause")
        # menuD

os.system("pause")
