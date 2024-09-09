x = 1 

def escopo():
    #global faria a manipulação do valor de x 
    #global x
    x = 10
    
    def outra_funcao():
        x = 11
        y = 2
        print(x. y)
        
    outra_funcao()
    print(x)
    
print(x)
escopo()
print(x)


def soma(x, y):
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)