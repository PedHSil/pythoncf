import enum

#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    BAIXO = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção inválida. Use "esquerda" ou "direita"')
    
    print(f'Movendo para {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover('lado')