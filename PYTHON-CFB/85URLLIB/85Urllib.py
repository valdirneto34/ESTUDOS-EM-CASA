from urllib import request

pagina = request.urlopen("https://www.google.com.br")
texto = pagina.read()
print(f'{texto}\n')

texto = str(texto)

dado1 = texto[0:16]
inicio = texto.find(dado1)
texto2 = texto[inicio+12:inicio+12+4]

print(f'\n{dado1}\n')
print(f'{inicio}\n')
print(f'{texto2}\n')
