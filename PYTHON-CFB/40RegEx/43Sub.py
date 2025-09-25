import re  # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res1 = re.sub(" ", "-", texto)
res2 = re.sub(",", ".", res1)

print(f'Res1: {res1}')
print(f'Res2: {res2}')
