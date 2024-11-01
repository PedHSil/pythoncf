'''Desenvolva um programa para determinar a média geral do aluno. O mesmo deverá receber o nome
do aluno, as 2 notas obtidas do aluno nas 2 avaliações. Calcular a média de aproveitamento, usando a
fórmula da Media e escrever o conceito do aluno de acordo com a tabela de conceitos.
Média é dada pela fórmula:
MG = (NP1*4 + NP2*6) / 10'''

print(f'Pedro Henrique da Silva – G76CHI3')

def calcular_media(nome, nota1, nota2):
    mg = (nota1*4 + nota2*6) /10
    
    if mg >= 9 and mg <= 10:
        print(f'Aluno: {nome}, Média Geral: {mg}, Situação: Aprovado!')
    elif mg >= 7 and mg < 9:
        print(f'Aluno: {nome}, Média Geral: {mg}, Situação: Aprovado!')
    elif mg >= 3 and mg < 7:
        print(f'Aluno: {nome}, Média Geral: {mg}, Situação: Exame!')
    elif mg >= 0 and mg < 3:
        print(f'Aluno: {nome}, Média Geral: {mg}, Situação: DP!')

        
name = str(input('Digite seu nome por favor: '))

np1 = float(input("Digite sua primeira nota: "))
np2 = float(input("Digite sua segunda nota: "))

calcular_media(name, np1, np2)