'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

# USEI A TABELA DE 2018

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 
        'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print('-=' * 60)
print(f'Lista de times do Brasileirão: {times}.')
print('-=' * 60)
print(f'Os 5 primerios colocados: {times[0:5]}.')
print('-=' * 60)
print(f'Os 4 últimos colocados: {times[-4:]}.')
print('-=' * 60)
print(f'Times em ordem alfabética: {sorted(times)}.')
print('-=' * 60)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª posição.')
print('-=' * 60)
