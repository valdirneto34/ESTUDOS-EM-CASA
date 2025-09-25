'''Crie um programa onde o usuário possa digitar cinco valores numéricos 
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

lista = []
for c in range(0, 5):
    num = (int(input(f'Digite um valor {c}: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        posi = 0
        while posi < len(lista):
            if num <= lista[posi]:
                lista.insert(posi, num)
                print(f'Adicionado na posição {posi} da lista...')
                break
            posi += 1
print('-='*30)
print(f'Valores digitados: {lista}')
