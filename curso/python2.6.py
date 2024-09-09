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

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))


for chave in pessoa():
    print(chave)