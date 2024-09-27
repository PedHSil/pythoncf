nome = input('Qual é o seu nome: ')
idd = input('Qual é a sua idade: ')

if nome and idd:
    print(f'Seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras') #contagem de caracteres 
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Você não digitou nome ou idade.')
    exit()
