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

##############################################################

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar()


s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')
print(s1('Luiz'))
print(s2('Luiz'))

##############################################################

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar()


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')
print(falar_bom_dia('Luiz'))

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_boa_noite(nome))