import random

def jogar():
    print("++++++++++++++++++++++++++++++++")
    print("bem vindo ao jogo de adivinhacao")
    print("++++++++++++++++++++++++++++++++")

    Numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000


    print("Niveis de dificuldade")
    print("(1) facil / (2) medio / (3) dificil")

    nivel = int((input("Escolha o nivel de dificuldade: ")))

    if (nivel == 1):
        print("Voce escolheu nivel facil")
        total_de_tentativas = 20
    elif(nivel == 2):
        print("Voce escolheu nivel medio")
        total_de_tentativas = 10
    elif(nivel == 3):
        print("Voce escolheu nivel dificil")
        total_de_tentativas = 5
    else:
        print("Numero invalido de dificuldade")


    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chutestr = input("Digite o numero entre 1 e 100: ")
        print("voce digitou", chutestr)
        chute = int(chutestr)

        if (chute < 1 or chute > 100):
            print("digite um numero entre 1 e 100")
            continue

        acertou = Numero_secreto == chute
        maior = chute > Numero_secreto
        menor = chute < Numero_secreto

        if (acertou):
            print("Voce acertou")
            print(f"voce fez {pontos} pontos")
            break
        else:
            if (maior):
                print("voce errou! seu chute foi maior")
            elif (menor):
                print("voce errou! seu chute foi menor")
        pontos_perdidos = abs(Numero_secreto - total_de_tentativas)
        pontos = pontos - pontos_perdidos
        print(f"voce esta com {pontos}")

    print("fim de jogo")

if(__name__ == "__main__"):
    jogar()