'''Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, nota 1 e
nota 2. O sistema deverá informar a ele as seguintes mensagens:
a) Se a média for maior ou igual a sete: Parabéns, você está aprovado!
b) Se a média for menor que sete: Você ainda tem uma chance! Estude mais para o
exame.'''

print(f'Pedro Henrique da Silva – G76CHI3')

def calcular_media():
    def entrada_dados():
        nome = input('Digite seu nome por favor: ')
        ra = int(input('Digite seu RA por favor: '))
        return nome, ra

    def calcular(nota1, nota2):
        return (nota1 + nota2) / 2

    def verificar_aprovacao(media, nome):
        if media >= 7:
            print(f'{nome}, sua média foi de {media}, parabéns, você foi aprovado!')
        else:
            print(f'{nome}, sua média foi de {media}, você ainda tem mais uma chance, estude mais para o exame')

    def salvar_media(media):
        with open('media.txt', 'w') as file:
            file.write(str(media))

    # Fluxo principal
    nome, ra = entrada_dados()

    while True:
        nota1 = float(input('Digite sua nota 1 por favor: '))
        nota2 = float(input('Digite sua nota 2 por favor: '))

        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            media = calcular(nota1, nota2)
            verificar_aprovacao(media, nome)
            salvar_media(media)
            break
        else:
            print(f'As notas, {nota1} e {nota2}, inseridas não são compatíveis com os valores que utilizamos para média geral!')

# Chama a função principal
calcular_media()
