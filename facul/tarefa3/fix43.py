'''Altere o algoritmo anterior (Fix32) para que o usuário entre com a nota do exame. Lembre-se
que deve se realizar a média aritmética entre a média e a nota do exame. O sistema deverá
informar a ele as seguintes mensagens:
a) Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está
aprovado.
b) Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o
mínimo necessário.
'''
# Abrindo o arquivo e lendo o valor da média
with open('media.txt', 'r') as file:
    media = float(file.read())

print(f'A média importada do arquivo fix42.py foi: {media}')


print(f'Pedro Henrique da Silva – G76CHI3')

def calcular_media(num):

    mediaaritimetica = (media + num) / 2
    

    if mediaaritimetica >= 5:
        print(f'{mediaaritimetica:.1f}, Parabéns, você aproveitou a sua chance! Está aprovado!')
    else:
        print(f'{mediaaritimetica:.1f}, estude mais para a próxima. Você não alcancou o mínimo necessário!')

num = float(input('Digite a nota do seu exame por favor: '))

calcular_media(num)