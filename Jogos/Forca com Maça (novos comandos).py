import random

def jogar(true=None):

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas =inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou): #Equanto nao enforcou nem acertou o jogo continua (ou seja, enquanto true continua executando)

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
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



def imprime_mensagem_abertura():
    print("++++++++++++++++++++++++++++++++")
    print("+++BEM VINDO AO JOGO DA FORCA+++")
    print("++++++++++++++++++++++++++++++++")
    print()
    print("Adivinhe qual a palavra. Voce pode errar 6 vezes")
    print()

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # chamando o arquivo de palavras do bloco de notas previamente criado
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # limpando os espacos
        palavras.append(linha)  # adicionar o que tiver na linha dentro da lista "palavras"

    arquivo.close()  # nao pode esquecer de fechar o arquivo depois que ele foi usado

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper().strip()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] #repare como "letra" foi uma variavel que não foi determinada. Qualquer coisa que colocar no lugar de "letra" ainda vai fucionar

def pede_chute():
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()  # para tirar espacos que venham a ser digitados antes ou depois no chute
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1

if (__name__ == "__main__"):
    jogar()
