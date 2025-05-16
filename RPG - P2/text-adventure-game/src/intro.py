import time
import os
import sys


# Criar jogador e nomear


def menu():
    
    print('''
 ██▓     █    ██ ▒███████▒   ▓█████      ██████  ▄▄▄       ███▄    █   ▄████  █    ██ ▓█████ 
▓██▒     ██  ▓██▒▒ ▒ ▒ ▄▀░   ▓█   ▀    ▒██    ▒ ▒████▄     ██ ▀█   █  ██▒ ▀█▒ ██  ▓██▒▓█   ▀ 
▒██░    ▓██  ▒██░░ ▒ ▄▀▒░    ▒███      ░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██  ▒██░▒███   
▒██░    ▓▓█  ░██░  ▄▀▒   ░   ▒▓█  ▄      ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▓▓█  ░██░▒▓█  ▄ 
░██████▒▒▒█████▓ ▒███████▒   ░▒████▒   ▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒▒█████▓ ░▒████▒
░ ▒░▓  ░░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒   ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░
░ ░ ▒  ░░░▒░ ░ ░ ░░▒ ▒ ░ ▒    ░ ░  ░   ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░░▒░ ░ ░  ░ ░  ░
  ░ ░    ░░░ ░ ░ ░ ░ ░ ░ ░      ░      ░  ░  ░    ░   ▒      ░   ░ ░ ░ ░   ░  ░░░ ░ ░    ░   
    ░  ░   ░       ░ ░          ░  ░         ░        ░  ░         ░       ░    ░        ░  ░
                 ░                                                                           
''')
    
    print(r"""                              ||||||||{ 1. Jogar }||||||||""")
    print(r"""                              ||||||||{ 2. Sair  }||||||||""")
    print("\n>>  ", end="")
    jogar = input()
    

    if jogar == "1":
        return True
    else:
        input("\n~~ Você escolheu sair do jogo. Pressione qualquer tecla para encerrar... ")
        exit()
        
menu()
os.system('cls' if os.name == 'nt' else 'clear')    


def narracao_intro():
    narrativa = [
        "\nHá muito tempo, antes que as estrelas esquecessem seus nomes...",
        "O continente de Aeloria florescia sob o olhar da Deusa Lumina.",
        "A Espada Estelar, forjada pelas mãos dos Filhos da Aurora, mantinha o equilíbrio entre luz e trevas.",
        "Mas a ambição dos homens foi maior que sua fé...",
        "O Lorde Varkas, seduzido pelo sussurro das sombras, traiu a luz e rasgou o véu da eternidade.",
        "Em sua queda, arrastou consigo reinos inteiros, afundando o mundo em eras de escuridão e sangue.",
        "Somente os Vigias da Brumia permaneceram firmes, guardiões silenciosos de uma esperança esquecida.",
        "E agora, enquanto a Noite Eterna se aproxima...",
        "O último dos Vigias desperta de um sono forçado, acorrentado sob as ruínas do Templo da Aurora.",
    ]

    for linha in narrativa:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)
        
narracao_intro()
os.system('cls' if os.name == 'nt' else 'clear')

def narracao1():
    
    narrativa1 = [
        f"Kael é o Vigia da Brumia.",
        "Seu corpo, uma sombra do que era, agora é um eco de dor e solidão.",
        "Mas dentro dele, uma centelha de esperança ainda brilha.",]
    
    for linha in narrativa1:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(4)
narracao1()
os.system('cls' if os.name == 'nt' else 'clear')
    
def narracao2():

    narrativa2 = [
        f"Você deve fazer que Kael reuna os fragmentos da Espada Estelar e restaurar o equilíbrio em Aurora.",
        "\nMas cuidado...",
        "\nA escuridão não é apenas uma força externa. Ela também habita dentro de nós.",
        "E as escolhas podem ser mais difícil do que parece.",]
    
    for linha in narrativa2:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(4)
narracao2()
os.system('cls' if os.name == 'nt' else 'clear')


