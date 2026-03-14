from rich import print
from rich.panel import Panel


class Churrasco:
    consumo_padrao: float = 0.400
    preco_kg: float = 82.4

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.qtd = qtd

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.qtd} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.qtd * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.qtd

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.qtd} convidados[/]\n"
        conteudo += f"Cada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R${self.calcular_custo_total():,.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar."
        resp = Panel(conteudo, title=self.titulo, width=80)
        print(resp)


c1 = Churrasco("Churras dos Parças", 15)
c1.analisar()

c2 = Churrasco("Formatura da Turma SI241", 28)
c2.analisar()
