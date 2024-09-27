'''Desenvolva um programa que só permita o acesso a pessoas autorizadas (professor, via
autenticação) para posteriormente realizar a média do aluno. Para isto Considere o programa
criado no Fix44.
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois
faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.'''

print('Pedro Henrique da Silva / CC / G76CHI3')

# Dicionário com credenciais de acesso
acesso_permitido = {
    'nome': 'Pedro H.',
    'senha': '133'
}

# Solicita o nome e a senha
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

if nome == acesso_permitido['nome'] and senha == acesso_permitido['senha']:
    print(f'Acesso permitido! Bem-vindo, {nome}.')
    
    while True:
        # Agora calcula a média dos alunos
        aluno = str(input('Digite o nome do aluno: '))
        ra = int(input('Digite o RA do aluno: '))
        turma = input('Digite a turma do aluno: ')
        np1 = float(input('Digite a primeira nota do aluno: '))
        np2 = float(input('Digite a segunda nota do aluno: '))
        
        mg = (np1 * 4 + np2 * 6) / 10
        
        print(f'\nNome: {aluno}\nRA: {ra}\nTurma: {turma}\nResultado Final: {mg}')
        
        continuar = input('As informações estão correta? (S/N): ')
        
        if continuar.lower() == 's':
            continue
        
        else:
            break
        
else:
    print('Acesso negado! Nome ou senha incorretos.')