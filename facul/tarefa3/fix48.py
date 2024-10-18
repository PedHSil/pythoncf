'''Elabore um programa em Python que o usuário entre com seu e seu salário. Se o salário for
menor ou igual a R$1500,00 coloque um acréscimo de 20% de aumento. Se for maior que
R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 5%
para os demais valores.
'''

print(f'Pedro Henrique da Silva – G76CHI3')

def calcula_acrescimo(salario):
    if salario <= 1500:
        acrescimo = salario * 0.20
        novo_salario = salario + acrescimo
        print(f'Seu novo salário com acréscimo de 20% é: {novo_salario:.2f}')
        
    elif salario > 1500 or salario < 2500:
        acrescimo = salario * 0.10
        novo_salario = salario + acrescimo
        print(f'Seu novo salário com acréscimo de 10% é: {novo_salario:.2f}')
        
    elif salario > 2500:
        acrescimo = salario * 0.05
        novo_salario = salario + acrescimo
        print(f'Seu novo salário com acréscimo de 5% é: {novo_salario:.2f}')
        


salario = float(input('Digite seu salário por favor: '))
calcula_acrescimo(salario)