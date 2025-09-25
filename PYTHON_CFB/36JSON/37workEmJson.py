import json

carros_dictionary = {"marca": "honda", "modelo": "HRV", "cor": "prata"}
# dictionary -> objeto

carros_list = ["honda", "wolkswagem", "ford", "fiat", "chevrolet"]
# list -> array json

carros_tupla = ("honda", "wolkswagem", "ford", "fiat", "chevrolet")
# tupla -> array json

carros_j = json.dumps(carros_dictionary, indent=4,
                      separators=(":", "="), sort_keys=True)

print(carros_j)
print('=-'*40)

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
print(jogador)
print('=-'*40)
for dados in jogador.items():
    print(dados)
