print('Bem vindo a outro programa de python')
print('')
print('Precisamos que escolha tres numeros.')
num1 = float(input('coloque o primeiro numero por favor: '))
num2 = float(input('coloque o segundo numero por favor: '))
num3 = float(input('coloque o terceiro numero por favor: '))

maior = max(num1, num2, num3)

# Determina o menor número
menor = min(num1, num2, num3)

# Exibe os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")