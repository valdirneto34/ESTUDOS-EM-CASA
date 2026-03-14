from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-'*30}\n"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        resp = Panel(conteudo, title="Produto", width=35)
        print(resp)


p1 = Produto("Iphone 17 Pro Max", 16999.90)
p2 = Produto("Samsung Galaxy S26 Ultra", 9999.90)

p1.etiqueta()
p2.etiqueta()
