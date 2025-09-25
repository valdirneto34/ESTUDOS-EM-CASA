import json

carros = {"marca": "honda", "modelo": "HRV", "cor": "prata"}

carros_json = json.dumps(carros)

# carros = json.loads(carros_json)
# print(carros["marca"])
# print(carros["modelo"])

for k, v in carros.items():
    print(f'{k} - {v}')
print('-='*30)
print(carros_json)
