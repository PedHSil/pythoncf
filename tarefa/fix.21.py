'''
Faça um algoritmo com três variáveis numéricas (tipo int) que realize a média aritmética da 
multiplicação desses 3 valores. Mostre os resultados na tela. Os mesmos devem ser solicitados 
ao usuário, digite os valores via teclado.
'''

# Solicitando os valores ao usuário
num1 = float(input('Digite su primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
num3 = float(input('Digite a terceira nota: '))

# Foi colocado float pois caso o usuario coloque uma casa decimal e programa gera um erro
# Convertendo os valores para inteiro
num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

# Calculando a multiplicação dos três valores
multiplicacao = num1_int * num2_int * num3_int

# Calculando a média aritmética da multiplicação
media_aritmetica = multiplicacao / 3

# Mostrando o resultado na tela
print(f'A multiplicação dos valores é: {multiplicacao}')
print(f'A média aritmética da multiplicação é: {media_aritmetica}')

print(f'Pedro Henrique da Silva – G76CHI3')
print()
print(f'Denner Moreira de Souza - G71EIE3')