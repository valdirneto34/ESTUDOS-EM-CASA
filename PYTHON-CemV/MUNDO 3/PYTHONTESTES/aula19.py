print('-='*30)
pessoas = {'nome':'Valdir','sexo':'M', 'idade':20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(f'Keys: {pessoas.keys()}')
print(f'Values: {pessoas.values()}')
print(f'Itens: {pessoas.items()}')
print('-='*30)
for k in pessoas.keys():
    print(f'Key: {k}')
print('-='*30)
for v in pessoas.values():
    print(f'Value: {v}')
pessoas['nome'] = 'Luiz'
del pessoas['sexo']
pessoas['peso'] = 80.6
print('-='*30)
for k, v in pessoas.items():
    print(f'O {k} = {v}.')
print('-='*30)
