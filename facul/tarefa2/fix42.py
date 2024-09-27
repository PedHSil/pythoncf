'''Elaborar um algoritmo (programa) que leia as notas de 5 alunos e retorne a maior nota da turma.
Utilize a estrutura de controle while.'''


# Inicializa variáveis
aluno = 1
maior_nota = 0
menor_nota = 0

# Loop para ler as notas dos 5 alunos
while aluno <= 5:
    nota = float(input(f"Digite a nota do aluno {aluno}: "))
    
    # Verifica se a nota atual é maior que a maior nota registrada
    if nota > maior_nota:
        maior_nota = nota
    # Incrementa o aluno
    aluno += 1

    # Verifica se a nota atual é menor que a menor nota registrada
    if menor_nota == 0 or (menor_nota > 0 and nota < menor_nota):
        menor_nota = nota
# Exibe a maior nota da turma
print(f"A maior nota da turma é: {maior_nota}")
print(f"A menor nota da turma é: {menor_nota}")

