print("++++++++++++++++++++++++++++++++")
print("+++++Joguinhos do balacobaco++++")
print("++++++++++++++++++++++++++++++++")

print("[1] jogo de adivinhacao / [2] joga da forca")

jogo = int(input("Escolha seu jogo: "))

if(jogo == 1):
    print('Voce escolhe o jogo de adivinhacao')
    import adivinhacao2

elif(jogo == 2):
    print("Voce escolheu o jogo da forca")
    import Forca
else:
    print('Numero de jogo nao valido')

