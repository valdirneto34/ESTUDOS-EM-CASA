import sqlite3
from sqlite3 import Error


def ConexaoBanco():  # Criar Conexão
    caminho = "C:\\PYTHON\\banco\\agenda"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()


def inserir(conexao, sql):  # Inserir
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)


# nome = input("Digite o nome: ")
# telefone = input("Digite o telefone: ")
# email = input("Digite o email: ")

# vsql = "INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)VALUES('" + \
    nome+"','"+telefone+"','"+email+"')"


# inserir(vcon, vsql)


def deletar(conexao, sql):  # Deletar
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido!")


vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO=2"

# deletar(vcon, vsql)


def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado!")


vsql = "UPDATE tb_contatos SET T_NOMECONTATO='Blestornildo', T_TELEFONECONTATO='(31)91234-5678',T_EMAILCONTATO='bles@email.com.br' WHERE N_IDCONTATO=3"

# atualizar(vcon, vsql)


def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado


vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%no'"
res = consulta(vcon, vsql)
for r in res:
    print(r)
