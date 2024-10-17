class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
        
    
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna
    
@Multiplicar(10)
def soma(x, y):
    return x + y

dois2 = soma(2, 2)
print(dois2)

###################################################################

def meu_decorator(funcao):
    def wrapper():
        print("Antes de chamar a função")
        funcao()  # Chama a função decorada
        print("Depois de chamar a função")
    return wrapper

@meu_decorator
def saudacao():
    print("Olá, mundo!")

saudacao()
