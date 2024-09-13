'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso 
(p) ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

# Solicitando a altura ao usuário

altura = float(input('Digite sua altura: '))

# Verificando se o usuário é homem ou mulher

sexo = input('Qual seu sexo (M/F)? ')

# Calculando o peso ideal

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal:.2f} kg')
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal:.2f} kg')
else:
    print('Sexo inválido. Por favor, digite M para masculino ou F para feminino.')
    
print()
print(f'Pedro Henrique da Silva – G76CHI3')
print()
print(f'Denner Moreira de Souza - G71EIE3')