carros = ["HRV", "Polo", "Jetta", "Cruze",
          "Fusion", "Golf", "Focus", "Ônix", "Fit"]

itCarros = iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista!")
        break
