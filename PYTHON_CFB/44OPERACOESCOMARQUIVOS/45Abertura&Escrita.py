import re
import os

pasta = os.path.dirname(__file__)

nome = "teste2.txt"
f = open(pasta+"\\"+nome, "rt")

res = re.sub(" ", "-", f.readline())
f.close()

f = open(pasta+"\\"+nome, "wt")
f.write(res)
f.close()

print(res)

# RETIREI DO PATH
# C:\Users\valdi\AppData\Local\Programs\Python\Python312\Scripts\
