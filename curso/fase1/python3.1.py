lista = []
for numero in range(10):
    lista.append(numero)
    
lista = [
    numero*2 
    for numero in range(10)
   
]
print(list(range(10)))
print(lista)
print(list)

################################################################
print()
################################################################
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 30,},
    {'nome': 'p3', 'preco': 40,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
#print(*novos_produtos, sep='\n')
#p(novos_produtos)
lista = [n for n in range(10) if n < 5]
print(lista)