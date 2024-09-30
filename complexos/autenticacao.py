import json

def refazer(informacaos, informacao_refazer):
    if not informacaos:
        print("Nenhuma informação disponível para corrigir.")
        return

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
    informacaos.append(aluno_info)  # Adiciona o aluno corrigido à lista

    # Salvar as novas informações no arquivo JSON
    salvar(informacaos, CAMINHO_ARQUIVO)

def ler(informacoes, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe. Criando novo arquivo.')
        salvar(informacoes, caminho_arquivo)
    return dados


def salvar(informacaos, caminho_arquivo):
    # Salvando os dados no arquivo JSON
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(informacaos, arquivo, indent=2, ensure_ascii=False)
    print("Informações salvas com sucesso.")


CAMINHO_ARQUIVO = 'auteninfo.json'
informacaos = ler([], CAMINHO_ARQUIVO)  # Carrega as informações existentes do arquivo
informacao_refazer = []  # Histórico para alunos que foram corrigidos

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
        # Solicita as informações do aluno
        aluno = str(input('Digite o nome do aluno: '))
        ra = int(input('Digite o RA do aluno: '))
        turma = input('Digite a turma do aluno: ')
        np1 = float(input('Digite a primeira nota do aluno: '))
        np2 = float(input('Digite a segunda nota do aluno: '))
        
        # Calcula a média ponderada
        mg = (np1 * 4 + np2 * 6) / 10
        
        print(f'\nNome: {aluno}\nRA: {ra}\nTurma: {turma}\nResultado Final: {mg}')
        
        continuar = input('As informações estão corretas? (S/N): ')
        
        if continuar.lower() == 's':
            aluno_info = {
                'nome': aluno,
                'ra': ra,
                'turma': turma,
                'nota1': np1,
                'nota2': np2,
                'media': mg
            }
            informacaos.append(aluno_info)  # Adiciona o aluno à lista
            salvar(informacaos, CAMINHO_ARQUIVO)  # Salva as informações no arquivo JSON
        
        elif continuar.lower() == 'n':
            refazer(informacaos, informacao_refazer)  # Corrige os dados

else:
    print('Acesso negado! Nome ou senha incorretos.')
