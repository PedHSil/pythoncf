'''Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, nota 1 e
nota 2. O sistema deverá informar a ele as seguintes mensagens:
a) Se a média for maior ou igual a sete: Parabéns, você está aprovado!
b) Se a média for menor que sete: Você ainda tem uma chance! Estude mais para o
exame.'''

print(f'Pedro Henrique da Silva – G76CHI3')

def calcular_media():
    name = input('Digite seu nome por favor: ')
    ra = int(input('Digite seu RA por favor: '))

    while True:
        nota1 = float(input('Digite sua nota 1 por favor: '))
        nota2 = float(input('Digite sua nota 2 por favor: '))

        # Verifica se as notas estão dentro do limite permitido
        if nota1 <= 10 and nota2 <= 10:
            media = (nota1 + nota2) / 2  # Calcula a média

            if media >= 7:
                print(f'{name}, sua média foi de {media}, parabéns, você foi aprovado!')
            else:
                print(f'{name}, sua média foi de {media}, você ainda tem mais uma chance, estude mais para o exame')

            # Salva a média em um arquivo
            with open('media.txt', 'w') as file:
                file.write(str(media))
            break  # Sai do loop após calcular e exibir a média
        else:
            print(f'As notas, {nota1} e {nota2} inseridas, não são compatíveis com os valores que utilizamos para média geral!')

# Chama a função principal
calcular_media()
