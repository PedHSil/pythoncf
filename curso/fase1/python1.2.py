#        0    1   2   3
lista = [10, 20 ,30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista,'Removido', ultimo_valor)

#############################

#         0   1   2   3 
lista = [10, 20, 30, 40]
lista.append('Pedro')
nome = lista.pop()
lista.append(1234)
del lista[-1]
#lista.clear()
lista.insert(0, 5)
print(lista)

'''
append - adiciona um item ao final
isert - adiciona um item no indice escolhido
pop - remove do final ou do indice escolhido
del - apaga um indice
clear - apaga todos os itens da lista
extend - estende a lista
+ - concatena listas
Create Read Uptade Delete = (CRUD)
'''

############################
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)