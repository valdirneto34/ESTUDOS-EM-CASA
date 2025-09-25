import datetime

data = datetime.datetime.now()
nasc = datetime.datetime(2004, 8, 9)

print(f'{data.day}/{data.month}/{data.year}')
print(nasc.strftime("%A"))

'''
# %a texto dia da semana abreviado
# %A texto dia da semana
# %w num do dia da semana
# %d num dia do mes
# %b texto mês abreviado
# %B texto mês
# %m num do mes
# %y ano com dois digitos
# %Y ano com quatro digitos
# %H 00 - 23
# %I 00 - 12
# %p AM / PM
# %M minutos
# %S segundos
# %f microssegundos
# %j dia do ano 001 - 365
# %W número da semana do ano
'''
