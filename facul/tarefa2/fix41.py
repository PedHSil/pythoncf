'''Elaborar um algoritmo (programa) que calcule o valor fatorial de um número inteiro positivo.
Utilize a estrutura de controle for ...in .
Cálculo do fatorial, exemplo: fatorial de 5 = 5!=1x2x3x4x5= 120'''


n1 = float(input("digite um numero inteiro: "))

n1_int = int(n1)

def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

resultado = calcular_fatorial(n1_int)
print(f'o fatorial de {n1_int} é {resultado}')
