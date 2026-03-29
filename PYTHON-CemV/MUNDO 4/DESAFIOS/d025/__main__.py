from rich import print, inspect
from rich.table import Table
from transportes import *


def main():
    dist = 20

    entrega = Moto(dist)
    print(
        f"Frete de {type(entrega).__name__} para {dist}km = {entrega.calcular_frete()}")

    entrega = Caminhao(dist)
    print(
        f"Frete de {type(entrega).__name__} para {dist}km = {entrega.calcular_frete()}")
    dist = 80
    entrega = Caminhao(dist)
    print(
        f"Frete de {type(entrega).__name__} para {dist}km = {entrega.calcular_frete()}")

    entrega = Drone(dist)
    print(
        f"Frete de {type(entrega).__name__} para {dist}km = {entrega.calcular_frete()}")
    dist = 8
    entrega = Drone(dist)
    print(
        f"Frete de {type(entrega).__name__} para {dist}km = {entrega.calcular_frete()}")

    dist = 10
    tabela = Table(title="Tabela de fretes")
    tabela.add_column("Distância")
    tabela.add_column("Transporte")
    tabela.add_column("Frete")
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    tabela.add_row(f"{dist}Km", f"{type(viagem[0]).__name__}", f"{viagem[0].calcular_frete()}")
    tabela.add_row(f"{dist}Km", f"{type(viagem[1]).__name__}", f"{viagem[1].calcular_frete()}")
    tabela.add_row(f"{dist}Km", f"{type(viagem[2]).__name__}", f"{viagem[2].calcular_frete()}")

    print(tabela)


if __name__ == "__main__":
    main()
