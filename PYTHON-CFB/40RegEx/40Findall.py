import re  # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res1 = re.findall("Python", texto)
res2 = re.findall("so", texto)
res3 = re.findall("o", texto)

pesq = input("Pesquisar: ")
res4 = re.findall(pesq, texto)

qtde = len(res4)
print(f'\nRes1: {res1}')
print(f'Res2: {res2}')
print(f'Res3: {res3}')
print(f'Res4: {res4}')
print(f'Qtde: {qtde}\n')

for t in res4:
    print(t)
 #