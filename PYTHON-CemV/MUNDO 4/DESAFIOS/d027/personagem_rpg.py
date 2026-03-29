from abc import ABC, abstractmethod
from rich import print
from random import randint

class Personagem(ABC):

    golpes = ["Soco", "Pulo Giratório", "Golpe de Machado", "Bola de Fogo"]

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, Personagem: Personagem, forca):
        dano = randint(0, forca)
        golpe = self.golpes[randint(0, len(self.golpes) - 1)]
        texto = f"\n[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red bold]{Personagem.nome}[/]([cyan]{Personagem.vida}[/]) com um [blue]{golpe}[/] de força [cyan]{forca}[/]!"
        texto += f"\n[blue]{Personagem.nome}[/] recebeu [red]dano de [bold]{dano}[/][/]!"
        Personagem.receber_dano(dano)
        if Personagem.vida == 0:
            texto += f"\n[red bold]{Personagem.nome}[/] foi derrotado!"
        print(texto)


    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def curar(self):
        cura = randint(0, 100)
        texto = f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura}[/] de vida!"
        print(texto)
        self.vida += cura

class Mago(Personagem):
    def curar(self):
        cura = randint(0, 100)
        texto = f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura}[/] de vida!"
        print(texto)
        self.vida += cura