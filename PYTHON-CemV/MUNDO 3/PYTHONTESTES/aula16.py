lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
print(lanche)
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')


for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print('Comi pra caramba!')

print(sorted(lanche)) #COLOCA EM ORDEM A TUPLA
