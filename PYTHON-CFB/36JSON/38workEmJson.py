import json

'''
{   "nome": "Bruno",
    "time": "aviadores",
    "vivo": "True",
    "energia": 100,
    "mochila": ["pederneira", "corda", "linha", "arame"],
    "aeronaves": [
        {"tipo": "transporte", "habilidade": 80},
        {"tipo": "ataque", "habilidade": 100},
        {"tipo": "reconhecimento", "habilidade": 50}
    ]
}
'''

jogador_j = '{"nome": "Bruno","time": "aviadores","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronaves": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque", "habilidade": 100},{"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)

# chaves
for c in jogador:
    print(c)
print('-='*40)
# itens
for i in jogador.items():
    print(i)
print('-='*40)
# valores
for v in jogador.values():
    print(v)
print('-='*40)
# nome do jogador
print(jogador["nome"])
print('-='*40)
# itens da mochila
for im in jogador["mochila"]:
    print(im)
print('-='*40)
# aerovanes
for a in jogador["aeronaves"]:
    print(f'{a["tipo"]} - {a["habilidade"]}')
print('-='*40)
