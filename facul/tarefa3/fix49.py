'''O usuário deve digitar seu nome e sua idade. O sistema deverá informar as seguintes
mensagens:
Bem vindo NOME você é maior de idade.
Bem vindo NOME você é menor de idade.
Bem vindo NOME você é maior de 65 anos'''

print(f'Pedro Henrique da Silva – G76CHI3')

def idade(x, nome):
    if x >= 65:
        print(f'Bem vindo {nome}, você é maior de 65 anos')
    elif x >= 18:
        print(f'Bem vindo {nome}, você é maior de idade')
    else:
        print(f'Bem vindo {nome}, você é menor de idade')
        
        
nome = str(input('Digite seu nome por favor: '))

id = int(input('Digite sua idade por favor: '))

idade(id, nome)