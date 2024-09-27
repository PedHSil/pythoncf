nome = input("qual é o seu nome?")

num1 = float(input("Digite sua primeira nota "+nome+": "))
num2 = float(input("Qual foi sua segunda nota "+nome+": "))
num3 = float(input("Qual foi sua terceira nota "+nome+": "))
num4 = float(input("Qual foi sua quarta nota "+nome+": "))

media = (num1 + num2 + num3 + num4)/4

if media >= 7:
    print("Parabéns "+nome+", você foi aprovado com média:", media)  
else:
    print("Você foi reprovado "+nome+", com média:", media)