from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos.sort()

    def ficha(self):
        conteudo = f"Nome real: [black on blue] {self.nome} [/]\n"
        conteudo += "Jogos favoritos:"
        for num, j in enumerate(self.favoritos):
            conteudo += f"\n:video_game:  [blue]{j}[/]"
        resp = Panel(conteudo, title=f"Jogador <{self.nick}>", width=50)
        print(resp)


j1 = Gamer("Valdir de Souza", "Morfeu")
j1.add_favoritos("Apex Legends")
j1.add_favoritos("Free Fire")
j1.add_favoritos("Read Dead Redemption 2")
j1.add_favoritos("GTA V")
j1.add_favoritos("Call Of Duty WWII")
j1.ficha()

j2 = Gamer("Patrícia da Silva", "Shyraishi")
j2.add_favoritos("Overcooked")
j2.add_favoritos("Past Within")
j2.add_favoritos("Cuphead")
j2.add_favoritos("Overcooked 2")
j2.ficha()
