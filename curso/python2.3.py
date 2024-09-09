'''
Higher order functions
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao,'Bpm dia,' 'Luiz')
)

print(executa(saudacao, 'Boa noite', 'Maria'))



##############################################################

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar()


s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Luiz')
print(s1)
print(s2)