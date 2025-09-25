def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO! \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)
