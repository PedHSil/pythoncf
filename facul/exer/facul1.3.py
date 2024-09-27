print('Bem vindo a outro programa de python')
print('')
print('Precisamos que escolha dois numeros.')
num1 = float(input('coloque o primeiro numero por favor: '))
num2 = float(input('coloque o segundo numero por favor: '))

if num1 >= num2:
    print(f'O numero maior é: {num1}')  
else: 
    print(f'O numero maior é: {num2}')