'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam 
R$ 35,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a) comprar apenas latas de 18 litros;
b) comprar apenas galões de 3,6 litros;
c) misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias.'''

# 1L para 6 metros quadrados. A lata contem 18L que custa 80 reais
# em galoes de 3,6L tem o valor de 35 reais 
import math

area = float(input('Qual será o tamanho da área que será pintada em metros quadrados: '))

# 10% de folga à área total
area_com_folga = area * 1.10

# Calcula a quantidade de litros de tinta necessária (1 litro para cada 6 m²)
litros_necessarios = area_com_folga / 6

# Calcula a quantidade de latas de 18 litros necessárias e o custo
latas_necessarias = math.ceil(litros_necessarios / 18)
custo_latas = latas_necessarias * 80.00

# .ceil é utilizado para arredondar o numero para cima

# Calcula a quantidade de galões de 3,6 litros necessários e o custo
galoes_necessarios = math.ceil(litros_necessarios / 3.6)
custo_galoes = galoes_necessarios * 35.00

# Calcula a combinação de latas e galões para o menor custo possível
latas_mistas = math.floor(litros_necessarios / 18)
resto_litros = litros_necessarios - (latas_mistas * 18)

# .floor é utilizado para arredondar o numero para baixo

galoes_mistos = math.ceil(resto_litros / 3.6)
custo_misto = (latas_mistas * 80.00) + (galoes_mistos * 35.00)

# Exibe os resultados
print(f'\nPara pintar {area:.2f} m² com 10% de folga, serão necessários {litros_necessarios:.2f} litros de tinta.')
print(f'\nSituação A: Comprar apenas latas de 18 litros.')
print(f'Quantidade de latas: {latas_necessarias} - Custo total: R$ {custo_latas:.2f}')

print(f'\nSituação B: Comprar apenas galões de 3,6 litros.')
print(f'Quantidade de galões: {galoes_necessarios} - Custo total: R$ {custo_galoes:.2f}')

print(f'\nSituação C: Misturar latas e galões para o menor preço.')
print(f'Quantidade de latas: {latas_mistas} - Quantidade de galões: {galoes_mistos} - Custo total: R$ {custo_misto:.2f}')
