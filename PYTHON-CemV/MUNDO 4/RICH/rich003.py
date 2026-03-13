from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="right", style="red")
tabela.add_column("Preço", justify="center", style="blue")
tabela.add_row("Lápis", "R$3,50")
tabela.add_row("Borracha", "R$5,00")
tabela.add_row("Caderno", "R$27,99")
tabela.add_row("Bolsa", "R$199,90")

print(tabela)