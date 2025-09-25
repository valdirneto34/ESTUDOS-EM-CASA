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


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com sucesso!")
        # conexao.close()


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    # conexao.close()
    return res


def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro Por ID")
    print("5 - Consultar Registro Por Nome")
    print("6 - Sair")


def menuInserir():
    os.system("cls")
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO,T_EMAILCONTATO) VALUES ('" + \
        vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vcon, vsql)


def menuDeletar():
    os.system("cls")


def menuAtualizar():
    os.system("cls")


def menuConsultar():
    os.system("cls")


def menuConsultarNomes():
    os.system("cls")


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

vcon.close()
os.system("pause")
