'''Faça um algoritmo com duas variáveis numéricas (tipo int) que realize as 4 operações básicas 
(soma, subtração, multiplicação e divisão), mostre os resultados na tela. Os mesmos devem ser 
solicitados ao usuário, digite os valores via teclado.'''

num1 = float(input('Digite um numero inteiro por favor: '))
num2 = float(input('Digite um segundo numero por favor: '))
#foi colocado float pois caso o usuario coloque um numero com casa decimal, o codigo ira gerar um erro
num1_int = (num1)
num2_int = (num2)

soma = num1_int + num2_int
sub = num1_int - num2_int
mult = num1_int * num2_int 
div = num1_int / num2_int

print(f'a soma de {num1_int} + {num2_int} é {soma}')
print(f'a subtração de {num1_int} - {num2_int} é {sub}')
print(f'a multiplicação de {num1_int} * {num2_int} é {mult}')
print(f'a divisão de {num1_int} / {num2_int} é {div}')