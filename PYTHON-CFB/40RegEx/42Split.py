import re  # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res1 = re.split(" ", texto)
res2 = re.split("d", texto)

print(res1)
print(res1[2])
for t in res1:
    print(t)
print('-='*40)
print(res2)
print(res2[2])
for t in res2:
    print(t)
