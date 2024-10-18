'''Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
 (1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
 (2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
 (3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5'''
 
print(f'Pedro Henrique da Silva – G76CHI3')

def valores_absoluto(x):
    if x < 0:
        print(f'valor absoluto: {abs(x)}')
    elif x > 10:
        valor2 = float(input('digite outro valor: '))
        print(f'diferenca: {x - valor2}')
    else:
        print(f'valor dividido por 5: {x / 5}')
        
valor = float(input('digite um valor: '))

valores_absoluto(valor)