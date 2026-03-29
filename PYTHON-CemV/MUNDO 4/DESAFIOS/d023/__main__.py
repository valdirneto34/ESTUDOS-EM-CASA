from rich import print, inspect
from poligono import *

def main():
    p1 = Quadrado(12)

    print(f"Um quadrado de lado {p1.lado} tem perímetro {p1.perimetro():.1f} e área {p1.area():.1f}")

    p2 = Circulo(12)

    print(f"Um círculo de raio {p2.raio} tem perímetro {p2.perimetro():.1f} e área {p2.area():.1f}")

if __name__ == "__main__":
    main()