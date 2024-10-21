'''Elabore um programa em Python que o usuário entre com seu e seu salário. Se o salário for
menor ou igual a R$1500,00 coloque um acréscimo de 20% de aumento. Se for maior que
R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 5%
para os demais valores.
'''

print(f'Pedro Henrique da Silva – G76CHI3')

def calcula_acrescimo():
    def calcular_novo_salario(salario, percentual):
        return salario + (salario * percentual)

    def mostrar_resultado(salario, percentual):
        novo_salario = calcular_novo_salario(salario, percentual)
        print(f'Seu novo salário com acréscimo de {percentual * 100}% é: {novo_salario:.2f}')

    salario = float(input('Digite seu salário por favor: '))

    if salario <= 1500:
        mostrar_resultado(salario, 0.20)
    elif 1500 < salario < 2500:
        mostrar_resultado(salario, 0.10)
    else:
        mostrar_resultado(salario, 0.05)

# Chama a função principal
calcula_acrescimo()
