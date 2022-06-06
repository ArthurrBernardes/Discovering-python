def jogar(true=None):
    print("++++++++++++++++++++++++++++++++")
    print("+++BEM VINDO AO JOGO DA FORCA+++")
    print("++++++++++++++++++++++++++++++++")


    print("Adivinhe qual a palavra. Voce pode errar 6 vezes")

    palavra_secreta = "banana".upper() #upper para se caso o chute for com letra maiscula, ele aceitar
    letras_acertadas = ["_","_","_","_","_","_"]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou): #Equanto nao enforcou nem acertou o jogo continua (ou seja, enquanto true continua executando)

        chute = input("Chute uma letra: ")
        chute = chute.strip().upper() #para tirar espacos que venham a ser digitados antes ou depois no chute

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index] = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        print(f"Voce errou {erros} de 6 tentativas")

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if enforcou:
        print("VOCE PERDEU")
    else:
        print("PARABENS!!! VOCE GANHOU!!!")
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
