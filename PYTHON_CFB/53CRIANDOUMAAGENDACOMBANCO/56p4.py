import os
import sqlite3
from sqlite3 import Error


def ConexaoBanco():  # --------Conexão
    caminho = "C:\\PYTHON\\banco\\agenda"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(f'\033[32m{ex}\033[m')
    return con


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("\033[32mOperação Realizada com sucesso!\033[m")
        conexao.close()


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    conexao.close()
    return res


def menuPrincipal():
    os.system("cls")
    print("\033[36m", end='')
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro Por Nome")
    print("6 - Sair")
    resp = int(input("Digite uma opção:\033[m "))
    return resp


def menuInserir():
    vcon = ConexaoBanco()
    os.system("cls")
    vnome = input("\033[33mDigite o nome....:\033[m ")
    vtele = input("\033[33mDigite o telefone:\033[m ")
    vemai = input("\033[33mDigite o email...:\033[m ")
    vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO,T_EMAILCONTATO) VALUES ('" + \
        vnome+"','"+vtele+"','"+vemai+"')"
    query(vcon, vsql)
    vcon.close()


def menuDeletar():
    vcon = ConexaoBanco()
    os.system("cls")
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
    query(vcon, vsql)
    vcon.close()


def menuAtualizar():
    vcon = ConexaoBanco()
    os.system("cls")
    vid = input("Digite o ID do registro a ser alterado: ")
    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    print(r)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail = remail
    vsql = "UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"', T_TELEFONECONTATO='" + \
        vtelefone+"',T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO="+vid
    query(vcon, vsql)
    vcon.close()


def menuConsultar():
    vcon = ConexaoBanco()
    os.system("cls")
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"\033[34mID:\033[33m{r[0]:<3}", end=' ')
        print(f"\033[34mNOME:\033[33m{r[1]:<30}", end=' ')
        print(f"\033[34mTELEFONE:\033[33m{r[2]:<14}", end=' ')
        print(f"\033[34mE-MAIL:\033[33m{r[3]:<30}\033[m")
        vcont += 1
        if (vcont >= vlim):
            vcont = 0
            os.system("pause")
            os.system("cls")
    print("\033[32mFim da lista!\033[m")
    vcon.close()
    os.system("pause")


def menuConsultarNomes():
    vcon = ConexaoBanco()
    os.system("cls")
    vnome = input("Digite o nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"\033[34mID:\033[33m{r[0]:<3}", end=' ')
        print(f"\033[34mNOME:\033[33m{r[1]:<30}", end=' ')
        print(f"\033[34mTELEFONE:\033[33m{r[2]:<14}", end=' ')
        print(f"\033[34mE-MAIL:\033[33m{r[3]:<30}\033[m")
        vcont += 1
        if (vcont >= vlim):
            vcont = 0
            os.system("pause")
            os.system("cls")
    vcon.close()
    print("\033[32mFim da lista!\033[m")
    os.system("pause")


opc = 0
while opc != 6:
    opc = menuPrincipal()
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
        print("\033[32mPrograma Finalizado!\033[m")
        break
    else:
        print("\033[31mOpção inválida!\033[m")
        os.system("pause")


os.system("pause")
