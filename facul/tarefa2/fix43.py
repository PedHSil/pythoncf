'''Elaborar um algoritmo (programa) que determine se a pessoa está com no seu Peso Ideal (ou
não) e IMC.
Onde o usuário deverá digitar o peso, o sexo e a altura de uma determinada pessoa. Após a execução,
deverá exibir se esta pessoa está ou não com seu peso ideal. Veja tabela (a) e (b) da relação
peso/altura².
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois
faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.'''



peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

sexo = str(input('qual é o seu sexo M/F ? :  '))

imc = peso /( altura * altura)

if sexo == 'F':
    if imc < 19:
        print(imc)
        print(f'Para o {sexo}, vc está abaixo do peso!')
    elif imc > 19 and imc < 24:
        print(imc)
        print(f'Para o {sexo}, vc está no peso ideal!')
    elif imc >= 24:
        print(imc)
        print(f'Para o {sexo}, vc está no peso ideal!')

elif sexo == 'M':
    if imc < 20:
        print(imc)
        print(f'Para o {sexo}, vc está abaixo do peso!')
    elif imc > 20 and imc < 25:
        print(imc)
        print(f'Para o {sexo}, vc está no peso ideal!')
    elif imc >= 25:
        print(imc)
        print(f'Para o {sexo}, vc está acima do peso!')

else:
    print('O sexo informado não existe!')