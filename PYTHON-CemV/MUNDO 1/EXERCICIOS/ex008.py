#Leia um valor em metros e o exiba convertido em centimetros e milimetros.

m=float(input('Digite um valor em metros: '))
km=m / 1000
hectometros=m / 100
decametros= m / 10
decimetros= m * 10
centimetros=m * 100
milimetros=m * 1000
print('Quilômetros: {}'.format(km))
print('Hectômetros: {}'.format(hectometros))
print('Decâmetros: {}'.format(decametros))
print('Decímetros: {}'.format(decimetros))
print('Centímetros: {}'.format(centimetros))
print('Milímetros: {}'.format(milimetros))
