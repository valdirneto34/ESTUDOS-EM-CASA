frase = '   Curso em Vídeo Python   '
print(frase[9]) #mostra uma letra
print(frase[9:13]) #mostra letras do caractere 9 ao 12
print(frase[9:18:2]) #mostra letras do caractere 9 ao 17(de 2 em 2)
print(len(frase)) #numero de caracteres
print(frase.count('O')) #procura uma letra(diferencia O de o)
print(frase.strip()) #espaços do inicio e fim
print(frase.lstrip()) #espaços da esquerda
print(frase.rstrip()) #espaços da direita
print('Curso' in frase)
print(frase.count('o'))
print(frase.replace('Python', 'Android')) #troca uma palavra
frase = frase.replace('Python', 'Android') #mudei uma string
print('Curso' in frase) #fala se tem a palavra(responde com TRUE ou FALSE)
print(frase.find('Curso')) #procura os caracteres
print(frase.lower()) #todas as letras minusculas
print(frase.upper()) #todas as letras maiusculas
print(frase.title()) #letra do inicio de cada palavra maiuscula
print(frase.split()) #transforma em lista
dividido = frase.split() #criei uma variavel em forma de lista
print(dividido[0]) #mostrei o conjunto 0 da lista
print(dividido[0][3]) #mostrei o caractere 3 do conjunto 0 da lista
print(frase.capitalize()) # apenas uma letra maiuscula
print(frase.join(dividido)) #juntar coisas
