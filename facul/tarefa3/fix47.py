'''Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por
10 ou se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é
divisível por nenhum desses valores.
'''

print(f'Pedro Henrique da Silva – G76CHI3')

print("O numero inserido será verificado se pode ser divisivel por 10, 5 ou 2")

def divisivel(x):
    if valor % 10 == 0:
        print(f'{valor} é divisivel por 10')
    elif valor % 5 == 0:
        print(f'{valor} é divisivel por 5')
    elif valor % 2 == 0:
        print(f'{valor} é divisivel por 2')
    else:
        print(f'{valor} não é divisivel por nenhum dos valores')
    
valor = float(input('Digite um numero por favor: '))
divisivel(valor)