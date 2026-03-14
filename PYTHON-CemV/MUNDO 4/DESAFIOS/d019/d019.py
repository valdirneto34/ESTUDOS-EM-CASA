from rich import print
from time import sleep


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pag_atual = 1
        print(
            f"\n:book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você está na[/] [yellow]página {self.pag_atual}[/]")

    def fim_do_livro(self) -> bool:
        if self.pag_atual == self.paginas:
            return True
        else:
            return False

    def avancar_paginas(self, qtd=1):
        cont = 0
        print()
        for c in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pag_atual += 1
                print(f"Pág{self.pag_atual} :arrow_forward: ", end="")
                cont += 1
                sleep(0.3)
        print(
            f"[blue]Você avançou {cont} páginas e gora está na[/] [yellow]página {self.pag_atual}[/]")
        if self.fim_do_livro():
            print(
                f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")


l1 = Livro("Odeio Te Amar", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
l1.avancar_paginas(5)
