'''Elaborar um programa que determine o cálculo do salário e retorna o valor a ser pago conforme o número
de horas trabalhadas. Lembrando que as mesmas serão digitadas
Seguem as regras de negócio
Caso a quantidade de horas trabalhadas é menor ou igual a 40, o valor do salário é apenas multiplicando
a quantidade de horas pelo valor de cada hora trabalhada.
Caso o trabalhar tenha horas extras, é adicionado ao salário um valor pelas horas extras.
Dica utilizar a função calcular_pagamento (HT, VH)'''

print(f'Pedro Henrique da Silva – G76CHI3')

# HT -> horas trabalhadas e VH -> valor das horas

# Função para calcular o salário com base nas horas trabalhadas e no valor por hora

def calcular_pagamento(name, HT, VH):
    # Valor da hora extra é o dobro do valor hora normal
    valor_hora_extra = VH * 2
    
    if HT <= 40:
        salario = HT * VH
        print(f'{name}, seu salário semanal é de {salario:.2f} reais.')
    else:
        # Caso tenha horas extras, calcula a parte extra do salário
        horas_extras = HT - 40
        salario = (40 * VH) + (horas_extras * valor_hora_extra)
        print(f'{name}, seu salário semanal com as horas extras é de {salario:.2f} reais.')

# Entrada de dados do usuário
name = input('Digite o nome do funcionário, por favor: ')
ht = float(input('Quantas horas foram trabalhadas?: '))
vh = float(input('Qual é o valor da hora do funcionário?: '))

# Chamada da função
calcular_pagamento(name, ht, vh)
