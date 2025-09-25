import os

carros = []


class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot*0.8)
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print(f'\033[34mNome........:\033[m {self.nome}')
        print(f'\033[34mPotência....:\033[m {self.pot}')
        print(f'\033[34mVel. Máxima.:\033[m {self.velMax}')
        print(f'\033[34mLigado......:\033[m {
              "Sim" if self.ligado == True else "Não"}')


def Menu():
    os.system("cls") or None
    print("\033[36m1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair")
    print(f'Quantidade de carros: {len(carros)}')
    opc = int(input('Digite uma opção:\033[m '))
    return opc


def NovoCarro():
    os.system("cls") or None
    n = str(input("\033[33mNome do Carro.....: \033[m"))
    p = int(input("\033[33mPotência do Carro.: \033[m"))
    car = Carro(n, p)
    carros.append(car)
    print("\033[32mNovo Carro criado!\033[m")
    os.system("pause")


def informacoes():
    os.system("cls") or None
    n = int(
        input("\033[33mInforme o número do Carro que deseja ver as informações: \033[m"))
    try:
        carros[n].info()
    except:
        print("\033[31mCarro não existe na lista!\033[m")
    os.system("pause")


def excluirCarro():
    os.system("cls") or None
    n = int(
        input("\033[33mInforme o número do Carro que deseja excluir: \033[m"))
    try:
        del carros[n]
    except:
        print("\033[31mCarro não existe na lista!\033[m")
    else:
        print("\033[32mCarro excluído!\033[m")
    os.system("pause")


def ligarCarro():
    os.system("cls") or None
    n = int(
        input("\033[33mInforme o número do Carro que deseja ligar: \033[m"))
    try:
        carros[n].ligar()
        print('\033[32mCarro ligado!\033[m')
    except:
        print("\033[31mCarro não existe na lista!\033[m")
    os.system("pause")


def desligarCarro():
    os.system("cls") or None
    n = int(
        input("\033[33mInforme o número do Carro que deseja desligar: \033[m"))
    try:
        carros[n].desligar()
        print('\033[32mCarro desligado!\033[m')
    except:
        print("\033[31mCarro não existe na lista!\033[m")
    os.system("pause")


def listarCarros():
    os.system("cls") or None
    p = 0
    print('\033[35m', end='')
    for c in carros:
        print(f'\033[35m{p}\033[m - \033[34m{c.nome}\033[m')
        p += 1
    print('\033[m')
    os.system("pause")


while True:
    ret = Menu()
    if ret == 1:
        NovoCarro()
    elif ret == 2:
        informacoes()
    elif ret == 3:
        excluirCarro()
    elif ret == 4:
        ligarCarro()
    elif ret == 5:
        desligarCarro()
    elif ret == 6:
        listarCarros()
    elif ret == 7:
        os.system("cls")
        print("\033[33mPrograma finalizado!\033[m")
        break
    else:
        print("\033[31mOpção inválida!\033[m")
        os.system("pause")
        ret = Menu()
