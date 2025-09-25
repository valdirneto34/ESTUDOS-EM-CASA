brasil1 = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
estado3 = {'uf':'Minas Gerais', 'sigla':'MG'}
estado4 = {'uf':'Goiás', 'sigla':'GO'}
brasil1 += estado1, estado2, estado3, estado4
print('=-'*20)
for es in brasil1:
    print(f'{es["uf"]}: {es["sigla"]}')
print('=-'*20)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)
print('=-'*20)
for estado in brasil:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}.')
print('=-'*20)