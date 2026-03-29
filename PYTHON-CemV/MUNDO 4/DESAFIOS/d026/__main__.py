from funcionarios import *

def main():
    f1 = FuncionarioHorista("Paulo", 12, 200)
    f1.calcular_sal()
    f1.analisar_sal()

    f2 = FuncionarioMensalista("Amanda", 9500)
    f2.calcular_sal()
    f2.analisar_sal()


if __name__ == "__main__":
    main()