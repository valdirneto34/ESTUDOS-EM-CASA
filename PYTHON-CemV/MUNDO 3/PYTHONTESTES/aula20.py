def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos+=1


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}!')
    print('\033[1;97m-\033[m'*50)


#Programa Principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print('\033[1;97m-\033[m'*50)
print(valores)
print('\033[1;97m-=\033[m'*25)
soma(5, 2)
soma(2, 9, 4)