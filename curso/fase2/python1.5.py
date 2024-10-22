# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(calendar.calendar(2024))
#print(calendar.month(2024, 10))
#for week in calendar.monthcalendar(2024, 10):
    #print(enumerate(week))
'''for day in week:
    if day == 0:
        continue
    print(day)'''
    