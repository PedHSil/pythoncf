frase = '                  olha so que,                coisa interessante                            '
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)
#strip corta o espaço do começo e no fim da string


frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
