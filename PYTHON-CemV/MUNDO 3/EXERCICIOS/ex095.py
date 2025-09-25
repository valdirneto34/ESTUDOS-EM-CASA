'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = {}
partidas = []
time = []
print('\033[1;32m-=\033[1;97m'*30)
while True:
    totalgols = gol = 0
    jogador['Nome'] = str(input("\033[1;97mNome do(a) Jogador(a): ")).title().strip()
    tot = int(input(f'Nº de partidas de {jogador["Nome"]}: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na {c+1}ª partida: ")))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('\033[1;97mQuer continuar: [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('\033[1;31mOpção inválida...', end=' ')
    if resp == 'N':
        print('-='*30)
        print('\033[1;32mJOGADORES CADASTRADOS\033[1;97m'.center(50))
        c = 0
        for jogador in time:
            c += 1
            espaco = 12 - len(jogador["Nome"])
            print(f'N°{c}   Nome: {jogador["Nome"]}', end=espaco*' ')
            print(f'Gols: {jogador["Gols"]}', end=espaco*' ')
            print(f'Total: {jogador["Total"]}')
        break
    print('\033[1;97m-' * 40)
print('\033[1;97m-' * 40)

while True:
    busca = int(input('\033[1;97mMostrar dados de qual jogador? (999 p/ parar) '))
    if busca == 999:
        print('\033[1;33m==================>PROGRAMA ENCERRADO<======================')
        break
    elif busca > len(time) or busca <= 0:
        print(f'\033[1;31mERRO! Não existe jogador com código {busca}!')
    else:
        print(f'\033[1;34m-- LEVANTAMENTO DO JOGADOR(A) {time[busca-1]["Nome"]} --\033[1;97m')
        for jogo, goals in enumerate(time[busca-1]["Gols"]):
            print(f'    No {jogo+1}º jogo fez {goals} gol(s).')
    print('\033[1;97m-' * 40)
print('\033[1;97m<< VOLTE SEMPRE >>\033[m'.center(60))
