from rich import print
from rich import inspect


class Funcionario:
    empresa = "Nexus Automação"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}."


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentar())
# inspect(c1, methods=True)

c2 = Funcionario("Pedro", "TI", "Desenvolvedor")
print(c2.apresentar())
#inspect(c2)
