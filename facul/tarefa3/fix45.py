'''Elabore um programa em PYTHON, que mostre os descontos concedidos pela loja ABC em
suas mercadorias. 
Em compras acima de R$ 300,00 forneça 20% de desconto, entre R$ 200,00 a R$ 299,99
desconto de 10% e abaixo de R$ 199,99 o desconto será de 5%. 
Mostre na tela o valor total e o valor final a pagar (com o desconto). 
Solicite ao usuário que digite os valores via teclado.
'''

print(f'Pedro Henrique da Silva – G76CHI3')

def compra(valor):
    if valor >= 300.00:
        desconto = valor * 0.20
        valorTotal = valor - desconto
        print(f'valor da sua compra foi: {valor:.2f}')
        print(f'com um desconto de: {desconto:.2f}')
        print(f'tendo como um valor total: {valorTotal:.2f}')
    elif valor >= 200.00 and valor < 299.99:
        desconto = valor * 0.10
        valorTotal = valor - desconto
        print(f'valor da sua compra foi: {valor:.2f}')
        print(f'com um desconto de: {desconto:.2f}')
        print(f'tendo como um valor total: {valorTotal:.2f}')
    elif valor <= 199.99:
        desconto = valor * 0.05
        valorTotal = valor - desconto
        print(f'valor da sua compra foi: {valor:.2f}')
        print(f'com um desconto de: {desconto:.2f}')
        print(f'tendo como um valor total: {valorTotal:.2f}')
    
valorCompra = float(input('qual é o valor da sua compra?: '))
valorCompra = compra(valorCompra)