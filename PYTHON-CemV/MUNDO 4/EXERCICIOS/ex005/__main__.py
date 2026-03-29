from rich import print, inspect
from classes import Aluno, Professor, Funcionario


def main():
    a1 = Aluno("Valdir", 21, "Sistemas de Informação", "SI-241")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    # inspect(a1, methods=True)

    p1 = Professor("Fernando", 46, "Informática", "Mestre")
    p1.fazer_aniversario()
    p1.dar_aula()
    # inspect(p1, methods=True)

    f1 = Funcionario("Maria", 35, "Secretária", "Administração")
    f1.fazer_aniversario()
    f1.bater_ponto()
    # inspect(f1, methods=True)

if __name__ == "__main__":
    main()
