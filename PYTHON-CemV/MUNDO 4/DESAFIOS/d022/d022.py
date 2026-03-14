from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    vol_min: int = 1
    vol_max: int = 6

    def __init__(self, canal=1, vol=2):
        self.canal = canal
        self.vol = vol
        self.ligada = False

    def liga_desliga(self):
        self.ligada = not self.ligada

    def diminuirCanal(self):
        if self.ligada:
            if self.canal == ControleRemoto.canal_min:
                self.canal = ControleRemoto.canal_max
            else:
                self.canal -= 1

    def aumentarCanal(self):
        if self.ligada:
            if self.canal == ControleRemoto.canal_max:
                self.canal = ControleRemoto.canal_min
            else:
                self.canal += 1

    def diminuirVolume(self):
        if self.ligada:
            if self.vol != ControleRemoto.vol_min:
                self.vol -= 1

    def aumentarVolume(self):
        if self.ligada:
            if self.vol != ControleRemoto.vol_max:
                self.vol += 1

    def mostrar_tv(self):
        conteudo = ""
        if not self.ligada:
            conteudo = "[red]:prohibited: A TV está desligada[/]"
        else:
            conteudo = "CANAL  = "
            for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if c == self.canal:
                    conteudo += f"[white on yellow] {c} [/]"
                else:
                    conteudo += f" {c} "
            conteudo += "\n\nVOLUME = "
            for c in range(ControleRemoto.vol_min, ControleRemoto.vol_max + 1):
                if c <= self.vol:
                    conteudo += f"[black on green]  [/]"
                else:
                    conteudo += f"[black on white]  [/]"

        tv = Panel(conteudo, title="[ TV ]", width=30)
        print("\n\n\n")
        print(tv)


c = ControleRemoto()
while True:
    c.mostrar_tv()
    opc = str(input(f"< CH{c.canal} >   - VOL{c.vol} +   ")).strip()[0]
    match opc:
        case "0":
            break
        case "@":
            c.liga_desliga()
        case "<":
            c.diminuirCanal()
        case ">":
            c.aumentarCanal()
        case "-":
            c.diminuirVolume()
        case "+":
            c.aumentarVolume()
print(f"\n\n:hand_with_fingers_splayed: [green bold] OBRIGADO! VOLTE SEMPRE!![/] :hand_with_fingers_splayed:\n")
