''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expr = str(input('Digite uma expressâo numérica: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == (')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não está válida!')

#PODE CONTAR ERRADO
'''primeiro = expressao.count('(')
segundo = expressao.count(')')
if primeiro == segundo:
    print(f'Sua expressão {expressao} é válida!')
else:
    print(f'Sua expressão {expressao} não é válida!')
if primeiro > segundo:
    diferenca = primeiro - segundo
    if diferenca == 1:
        print(f'Falta {diferenca} parêntese fechando!')
    else:
        print(f'Faltam {diferenca} parênteses fechando!')
elif segundo > primeiro:
    diferenca = segundo - primeiro
    if diferenca == 1:
        print(f'Falta {diferenca} parêntese abrindo!')
    else:
         print(f'Faltam {diferenca} parênteses abrindo!')
'''