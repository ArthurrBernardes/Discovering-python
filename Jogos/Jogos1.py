import forca
import adivinhacao

def escolhe_jogo():
    print("++++++++++++++++++++++++++++++++")
    print("+++++Joguinhos do balacobaco++++")
    print("++++++++++++++++++++++++++++++++")

    print("[1] jogo de adivinhacao / [2] joga da forca")

    jogo = int(input("Escolha seu jogo: "))

    if(jogo == 1):
        print('Voce escolhe o jogo de adivinhacao')
        Adivinhacao1.jogar()
    elif(jogo == 2):
        print("Voce escolheu o jogo da forca")
        Forca1.jogar()
    else:
        print('Numero de jogo nao valido')

if (__name__ == "__main__"):
    escolhe_jogo()