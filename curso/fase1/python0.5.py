num1 = int(input('olá, por favor coloque um numero inteiro:  '))

if num1 == float:
    print('Você colocou um numero float.')
else:
    if num1 % 2 == 0:
        print(f'O numero {num1} é par.')
    else:
        print(f'O numero {num1} é impar.')

################################
entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'o numero {entrada_int} é {par_impar_texto}')
else:
    print('Você não colocou um número inteiro.')



# Exercício 2
horas = input('Que horas são? n precisa passar os minutos: ')

hora = int(entrada)

if horas >= 0 <= 11:
    print('Bom dia!')
elif horas >= 10 <= 18:
    print('Boa tarde!')
elif horas >= 18 <= 24:
    print('Boa noite!')
else:
    print('Hora inválida!')



################################################################

horas = input('Digite a hora em numeros inteiroas: ')

try:
    hora = int(entrada)

    if hora<= 0 and hora <= 11:
        print('Bom dia!')
    elif horas >= 10 <= 18:
        print('Boa tarde!')
    elif horas >= 18 <= 24:
        print('Boa noite!')

except:
    print('Você precisa digitar um número inteiro.')


# Exercício 3

nome = input('Qual é o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    if tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é longo')
else: 
    print('Você não colocou um nome.')
