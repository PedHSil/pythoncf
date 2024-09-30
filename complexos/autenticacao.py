import json

def refazer(informacaos, informacao_refazer):
    print("\nRefazendo as informações do aluno...\n")
    # Retirar a última informação incorreta e pedir a correção
    aluno_errado = informacaos.pop()  # Remove a última entrada de aluno
    informacao_refazer.append(aluno_errado)  # Salva no histórico de refazer

    # Solicitar novamente os dados do aluno
    aluno = input(f'Nome anterior: {aluno_errado["nome"]} - Digite o novo nome do aluno: ')
    ra = input(f'RA anterior: {aluno_errado["ra"]} - Digite o novo RA do aluno: ')
    turma = input(f'Turma anterior: {aluno_errado["turma"]} - Digite a nova turma do aluno: ')
    np1 = float(input(f'Nota 1 anterior: {aluno_errado["nota1"]} - Digite a nova nota 1: '))
    np2 = float(input(f'Nota 2 anterior: {aluno_errado["nota2"]} - Digite a nova nota 2: '))
    
    # Recalcular a média
    mg = (np1 * 4 + np2 * 6) / 10
    
    # Exibir o resultado corrigido
    print(f'\nNome: {aluno}\nRA: {ra}\nTurma: {turma}\nResultado Final: {mg}')
    
    # Salvar as informações corrigidas
    aluno_info = {
        'nome': aluno,
        'ra': ra,
        'turma': turma,
        'nota1': np1,
        'nota2': np2,
        'media': mg
    }
    informacaos.append(aluno_info) 

def ler(informacoes, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(informacoes, caminho_arquivo)
    return dados


def salvar(informacaos, caminho_arquivo):
    dados = informacaos
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(informacaos, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'auteninfo.json'
informacaos = ler([], CAMINHO_ARQUIVO)
informacao_refazer = []


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
        
        elif continuar.lower() == 'n':
            refazer(informacaos, informacao_refazer)
        
else:
    print('Acesso negado! Nome ou senha incorretos.')