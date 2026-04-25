from rich import print, inspect
from personagem_rpg import *

def main():
    p1 = Guerreiro("Megaman", 1000)
    p2 = Mago("Merlin", 5000)
    p3 = Guerreiro("Katos", 1500)

    p1.atacar(p2, 1000)
    p3.atacar(p1)
    p2.atacar(p3)

    p1.curar()
    p2.curar()

    p1.status_jogo()
    p2.status_jogo()
    p3.status_jogo()

if __name__ == "__main__":
    main()