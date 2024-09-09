
contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')

####################################################

contador = 0 

while contador <= 10:
    contador += 1

    if contador ==6:
        print('Não vou mostar o 6.')
        continue

    print(contador)

    if contador == 20:
        break

print('Acabou')

####################################################

qtd_linhas = 5
qtd_colunas = 5

linha = 1 
while linha <= qtd_linhas:
    coluna = 1
    print(linha)

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')