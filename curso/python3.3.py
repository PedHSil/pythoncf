try: 
    a = 18
    b = 0
   # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
except NameError:
    print('Erro: Variável não definida.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG', error)
    print('Nome', error.__class__.__name__)
except Exception:
    print('Erro: Ocorreu um erro inesperado.')
    
print('Continuar')

################################################################

try:
    print('Abrir arquivo')
    8/0
except ZeroDivisionError:
    print('Tentatiova de divisão por 0')
else:
    print('Arquivo aberto com sucesso') 
finally:
    print('Fechar arquivo')
    

################################################################

print(213/0)
raise ValueError ('Deu error')