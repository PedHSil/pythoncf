import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
        
p1 = Pessoa('Luiz', 'Otávio')
p2 = Pessoa('Maria', 'Joana')
p3 = Pessoa('Daniel', 'Silva')
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w' ) as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    print('ELE É O __MAIN__')   
    fazer_dump()