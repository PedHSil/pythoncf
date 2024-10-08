import json

from savejson import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    
    print(p1.nome, p1.sobrenome)
    print(p2.nome, p2.sobrenome)
    print(p3.nome, p3.sobrenome)
        
print(__name__)        
