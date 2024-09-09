'''pessoa = dict(nome = 'Pedro Henrique', sobrenome = 'silva')
print(pessoa, type(pessoa))'''

pessoa ={
    'nome': 'Pedro Henrique',
    'sobrenome': 'silva',    
    'idade': 19,
    'altura': 1.83,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 456},        
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
    
################################################################

pessoa = {}

pessoa['nome'] = 'PEDRO hENRIQUE'

print(pessoa)
print(pessoa['nome'])
