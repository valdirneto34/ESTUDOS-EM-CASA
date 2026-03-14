from rich import print


class Caneta:
    def __init__(self, cor="azul"):
        if cor == "azul":
            self.cor = "[blue]"
        elif cor == "verde":
            self.cor = "[green]"
        elif cor == "vermelha" or cor == "vermelho":
            self.cor = "[red]"
        else:
            self.cor = "[white]"
        self.tampada = True

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, texto):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{texto}[/]", end="")

    def quebrar_linha(self, qtd=1):
        print(qtd*"\n", end="")


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

# c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")
c3.quebrar_linha(5)
c1.destampar()
c1.escrever("Deu tudo certo!")