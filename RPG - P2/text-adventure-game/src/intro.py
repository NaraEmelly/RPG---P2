import time
import os
import sys
import colorama 
from colorama import Fore, Back, Style


# Criar jogador e nomear


def menu():
    
    logo = Fore.RED + '''
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
''' + Style.RESET_ALL
    largura = 30
    print(logo.center(largura))
    
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
        "O continente de Aurora florescia sob o olhar da Deusa Lumina.",
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

def historia_varkas():    
    varkas = [
        "Há muito tempo atras, no reino de Aurara,",
        "um jovem cavaleiro chamado Varkas convivia com os habitantes e era respeitado por todos.",
        "Desde pequeno, Varkas foi treinado pelos seus pais para proteger os inocentes,", 
        "seguindo os preceitos da Ordem da Luz, um grupo sagrado de guardiões que defendia o reino de ameaças mágicas e monstruosas da escuridão.",
        "Com o passar dos anos, Varkas reconhecido pelos seus feitos nas comunidades, foi chamado para participar da Ordem da Luz,",
        "tendo mais reconhecimento na sociedade,", 
        "mas a verdade é que o mundo nem sempre recompensa os bons.",
        "Durante uma missão para recuperar o mapa da espada da luz,",
        "Varkas e seu pelotão foram traídos pelos soldados do reino que temia o crescimento de seu poder e popularidade.", 
        "A emboscada matou todos os seus companheiros.",
        "Varkas sobreviveu, gravemente ferido, apenas para ser acusado de traição ao retornar.",
        "Humilhado publicamente, expulso da Ordem e rejeitado por aqueles que um dia o adoraram,", 
        "Varkas foi julgado por ter matado todos do pelotão,",
        "porem, Lumina viu a escuridão manipulando ele e o deixou sair ileso, por ter visto que ele não os matou,",
        "mas o jogou nas masmorras do reino,",
        "quando Varkas saiu, com seu ódio criou um grupo de ANTILUMINOS para fazer uma rebelião,",
        "contudo, seu grupo foi capturado, massacrado, torturado e morto pelos guardas imperiais da luz,",
        "fazendo ele ficar com um extremo ódio ascendente em seu peito,", 
        "despertando assim seu grandioso poder da escuridão e traindo completamente a luz,",  
        "com seu poder divino, ele destruiu vilas, templos e matou famílias e cidadãos inocentes,",
        "percebendo o quão forte ele era,",
        "decidiu se tornar um líder da escuridão e criar o seu império",
        "e agora ele deseja buscar a espada da luz para converte-la em trevas e criar um novo mundo",
    ]
    for linha in varkas:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)  
        
historia_varkas()
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


