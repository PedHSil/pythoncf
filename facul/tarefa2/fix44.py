'''Desenvolva um programa para determinar a média geral do aluno. O mesmo deverá receber o nome do
aluno, as 2 notas obtidas do aluno nas 2 avaliações. Calcular a média de aproveitamento, usando a
fórmula da Media e escrever o conceito do aluno de acordo com a tabela de conceitos.
Média é dada pela fórmula:
MG = (NP1*4 + NP2*6) / 10'''

print('Pedro Henrique da Silva / CC / G76CHI3')

nome = str(input('Digite seu nome por favor: '))

np1 = float(input('Digite sua nota da NP1: '))
np2 = float(input('Digite sua segunda nota da NP2: '))

mg = (np1 * 4 + np2 * 6) / 10

if mg >= 9 and mg <=10:
    print(f'{nome}, com uma {mg}, você APROVADO!')
elif mg >= 7 and mg < 9:
    print(f'{nome}, com uma {mg}, você APROVADO!')
elif mg >= 3 and mg < 7:
    print(f'{nome}, com uma {mg}, você está de EXAME!')
elif mg >= 0 and mg < 3:
    print(f'{nome}, com uma {mg}, você está de DP!')
else:
    print(f'As notas, {np1} e {np2} inseridas, não são compativas com os valores que utilizamos para Media geral!')