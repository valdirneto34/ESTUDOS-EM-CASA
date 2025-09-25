x = 10
try:
    print(x)
except NameError:
    print("X não definido!")
except:
    print("Erro desconhecido!")
else:
    print("Tudo certo!")
finally:
    print("Fim do Tratamento!\n")

'''num = -10
if num < 1:
    raise Exception("Valor não permitido!")'''

num1 = "Bruno"
if not type(num1) is int:
    raise Exception("Somente números permitidos!")
else:
    print(num1)
