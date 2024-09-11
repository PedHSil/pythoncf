'''Faça um algoritmo que mostre os descontos concedidos pela loja ABC em suas mercadorias. 
Em compras acima de 300,00 forneça 20% de desconto, para 200,00 desconto de 15% e acima 
de 100,00 o desconto será de 10%. Atribua valores as variáveis compra1, compra2 e compra3. 
Mostre na tela o valor total e o valor com o devido desconto. Os mesmos devem ser solicitados 
ao usuário, digite os valores via teclado.'''

# Solicitando os valores ao usuário
compra1 = float(input('Digite o valor da compra 1: '))
compra2 = float(input('Digite o valor da compra 2: '))
compra3 = float(input('Digite o valor da compra 3: '))

# Verificando os descontos para compra1
if compra1 > 300.00:
    desconto1 = compra1 * 0.20
elif compra1 > 200.00:
    desconto1 = compra1 * 0.15
elif compra1 > 100.00:
    desconto1 = compra1 * 0.10

# Verificando os descontos para compra2
if compra2 > 300.00:
    desconto2 = compra2 * 0.20
elif compra2 > 200.00:
    desconto2 = compra2 * 0.15
elif compra2 > 100.00:
    desconto2 = compra2 * 0.10

# Verificando os descontos para compra3
if compra3 > 300.00:
    desconto3 = compra3 * 0.20
elif compra3 > 200.00:
    desconto3 = compra3 * 0.15
elif compra3 > 100.00:
    desconto3 = compra3 * 0.10

# Calculando os valores com desconto
compra1_descontado = compra1 - desconto1
compra2_descontado = compra2 - desconto2
compra3_descontado = compra3 - desconto3

# Calculando o valor total e o valor total com desconto
valor_total = compra1 + compra2 + compra3
valor_total_descontado = compra1_descontado + compra2_descontado + compra3_descontado

# Mostrando os resultados na tela
print(f'Valor total da compra 1 com desconto: R$ {compra1_descontado:.2f}')
print(f'Valor total da compra 2 com desconto: R$ {compra2_descontado:.2f}')
print(f'Valor total da compra 3 com desconto: R$ {compra3_descontado:.2f}')
print(f'\nValor total das compras: R$ {valor_total:.2f}')
print(f'Valor total das compras com desconto: R$ {valor_total_descontado:.2f}')

print()
print(f'Pedro Henrique da Silva – G76CHI3')
print()
print(f'Denner Moreira de Souza - G71EIE3')