'''teste = list()
teste.append('Valdir')
teste.append(19)
print(teste)
print('-='*20)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('-='*20)

turma = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(turma[0][0])
print('-='*20)
print(turma[2][1])
print('-='*20)
for p in turma:
    print('=='*15)
    print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

tropa = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    tropa.append(dado[:])
    dado.clear()
print(tropa)

for p in tropa:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor +=1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
