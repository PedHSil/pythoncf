def multiplicar(*args):
    total = 0
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4,5)
print(multiplicacao)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero}par'
    return f'{numero}impar'



print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))



