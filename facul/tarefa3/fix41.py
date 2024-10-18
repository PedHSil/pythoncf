'''Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; 
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.'''
print(f'Pedro Henrique da Silva – G76CHI3')

import math

def processar_numero(num):
    numInt = int(num)

    if numInt <= 3:
        return numInt ** 2
    elif numInt == 4 or numInt == 9:
        return math.sqrt(numInt)
    elif numInt in [6, 7, 8]:
        return numInt / 9
    else:
        return "Número inválido"

# Recebe o número do usuário
num = float(input("Digite um número por favor: "))

# Chama a função e imprime o resultado
resultado = processar_numero(num)
print(resultado)