import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    dificuldade = input("Escolha a dificuldade (fácil, médio, difícil): ").strip().lower()
    
    if dificuldade == "fácil":
        minimo, maximo, max_tentativas = 1, 50, 15
    elif dificuldade == "médio":
        minimo, maximo, max_tentativas = 1, 100, 10
    else:
        minimo, maximo, max_tentativas = 1, 200, 7

    numero_secreto = random.randint(minimo, maximo)
    tentativas = 0

    while tentativas < max_tentativas:
        tentativa = int(input(f"Tente adivinhar o número entre {minimo} e {maximo} (Tentativas restantes: {max_tentativas - tentativas}): "))
        tentativas += 1
        
        if tentativa < numero_secreto:
            print("O número é maior. Tente novamente!")
        elif tentativa > numero_secreto:
            print("O número é menor. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
    else:
        print(f"Você não acertou. O número secreto era {numero_secreto}.")


jogo_adivinhacao()