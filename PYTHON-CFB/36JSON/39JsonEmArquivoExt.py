import json

with open(r'C:\Users\valdi\OneDrive\Documentos\CFB\PYTHON\36JSON\jogador.json') as f:
    jogador = json.load(f)

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
