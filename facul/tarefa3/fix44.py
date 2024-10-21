'''Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
(1) se o valor for 1 e 2, mostre o valor elevado ao cubo; 
(2) se o valor for múltiplo de 3 mostre o fatorial desse número; 
(3) se o valor for os valores 4, 5, 7 ou 8, mostre o valor dividido 9. Caso não seja nenhum
dos valores, informe como “valor inválido”.'''

print(f'Pedro Henrique da Silva – G76CHI3')

def umAoito():
    def cubo(valor):
        return valor ** 3

    def fatorial(valor):
        resultado = 1
        for i in range(1, valor + 1):
            resultado *= i
        return resultado

    def divisao_por_nove(valor):
        return valor / 9

    while True:
        num = float(input("Digite um número entre 1 e 8 por favor: "))
        numInt = int(num)

        if num > 8 or num < 1:
            print("Número inválido, por favor digite um valor entre 1 e 8.")
        else:
            if numInt == 1 or numInt == 2:
                resultado = cubo(numInt)
                print(f'O número {numInt} elevado ao cubo é {resultado}')
                break
            elif numInt == 3 or numInt == 6:
                resultado = fatorial(numInt)
                print(f'O fatorial de {numInt} é {resultado}')
                break
            elif numInt == 4 or numInt == 5 or numInt == 7 or numInt == 8:
                resultado = divisao_por_nove(numInt)
                print(f'O número {numInt} dividido por 9 é {resultado}')
                break
            else:
                print("Número inválido.")

umAoito()
