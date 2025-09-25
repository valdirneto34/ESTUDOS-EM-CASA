num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro número é maior.')
elif num2 > num1:
    print('O segundo número é maior.')
elif num1 == num2:
    print('Não existe valor maior, os números {} e {} são iguais.'.format(num1, num2))
    