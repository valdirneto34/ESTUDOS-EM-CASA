'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''

from moeda import __ini__

p = float(input('Digite o preço: R$'))
__ini__.resumo(p, 20, 12)
