from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    salario_min = 1612
    inss = 7.5

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_sal(self) -> float:
        pass

    def analisar_sal(self):
        total = self.calcular_sal()
        qtd_sal_min = total / Funcionario.salario_min
        texto = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${total:.2f}[/] e corresponde a [yellow]{qtd_sal_min:.1f} salários mínimos[/]."
        resp = Panel(texto, title="Análise Salarial", width=60)
        print(resp)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_sal(self):
        sal = self.valor_hora * self.qtd_horas
        return sal - (sal * Funcionario.inss / 100)


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_sal(self):
        return self.salario - (self.salario * Funcionario.inss / 100)

