'''Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
(1) se o valor for 1 e 2, mostre o valor elevado ao cubo; 
(2) se o valor for múltiplo de 3 mostre o fatorial desse número; 
(3) se o valor for os valores 4, 5, 7 ou 8, mostre o valor dividido 9. Caso não seja nenhum
dos valores, informe como “valor inválido”.'''

print(f'Pedro Henrique da Silva – G76CHI3')


def umAoito():
    while True:
        num = float(input("digite um numero entre 1 e 8 por favor: "))

        numInt = int(num)

        if num > 8:
            print("numero invalido, por favor digite um valor entre 1 e 8")
                    
        else:
            if numInt == 1 or numInt == 2:
                cubo = numInt ** 3
                print(f'O numero {numInt} elevado ao cubo é {cubo}')
                break
            elif numInt == 3 or numInt == 6:
                fatorial = 1
                contador = 1
                while contador <= numInt:
                    fatorial = fatorial * contador
                    contador = contador + 1
                print(f'O fatorial de {numInt} é {fatorial}')
                break
            elif numInt == 4 or numInt == 5 or numInt == 7 or numInt == 8:
                div = numInt / 9
                print(f'O numero {numInt} dividido por 9 é {div}')
                break
            else:
                print("numero invalido")
                
umAoito()