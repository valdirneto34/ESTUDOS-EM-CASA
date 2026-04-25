from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from random import randint, randrange


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange(0, len(self.golpes))]
            print(f"\n[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red bold]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com um [blue]{golpe}[/] de força [cyan]{forca}[/]!")
            alvo.receber_dano(forca)
            if alvo.vida == 0:
                texto += f"\n[red bold]{alvo.nome}[/] foi derrotado!"
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer!")

    def receber_dano(self, dano):
        fator = randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(
            f"\n[blue]{self.nome}[/] recebeu [red]dano de [bold]{fator}[/][/]!")

    @abstractmethod
    def curar(self):
        pass

    def status_jogo(self):
        texto = f"Nome: {self.nome}\n"
        texto += f"Vida: {self.vida} HP\n"
        texto += f"Golpes: "
        qtd_golpes = len(self.golpes)-1
        for c in range(0, qtd_golpes+1):
            texto += self.golpes[c]
            if c < qtd_golpes:
                texto += ", "
        status = Panel(f"[white]{texto}[/]", title="Status do Jogo", style="green", width=80)
        print(status)


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratório"]

    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        print(
            f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura}[/] de vida!")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de Luz", "Magia Estática"]

    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        print(
            f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura}[/] de vida!")
