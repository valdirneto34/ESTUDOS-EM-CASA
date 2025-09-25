# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar
# CONSIDERA US$1,OO=R$3,27

real=float(input('Digite quantos reais você tem na carteira:R$'))
dolares=real / 3.27
print('Você pode comprar {:.2f} dólares.'.format(dolares))
