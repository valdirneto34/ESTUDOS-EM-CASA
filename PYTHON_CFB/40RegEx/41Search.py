import re  # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"


res1 = re.search("canal", texto)
# \AC começa com "A"

if (res1 != None):
    print(f'Início: {res1.start()} - Fim: {res1.end()}')
    print(f'Tam: {res1.end()-res1.start()}')
else:
    print('Não encontrado!')
