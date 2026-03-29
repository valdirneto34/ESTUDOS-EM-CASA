from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass


class Caminhao(Transporte):
    fator = 1.2

    def calcular_frete(self):
        if self.distancia < 50:
            return "Raio mínimo é de 50km"
        else:
            return f"R${self.distancia * Caminhao.fator:.2f}"


class Moto(Transporte):

    fator = 0.5

    def calcular_frete(self):
        return f"R${self.distancia * Moto.fator:.2f}"


class Drone(Transporte):
    fator = 9.5

    def calcular_frete(self):
        if self.distancia > 10:
            return "Raio máximo é de 10km"
        else:
            return f"R${self.distancia * Drone.fator:.2f}"
