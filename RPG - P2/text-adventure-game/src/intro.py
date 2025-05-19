import time
import os
import sys
import colorama 
from colorama import Fore, Back, Style


# Criar jogador e nomear


def menu():
    
    
    print(Fore.RED + r"""
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
""" + Style.RESET_ALL ) 
    
    print(Style.BRIGHT + Fore.RED + r"""
                                                                                            ◤————————————————————◥ 
                                                                                            |     1. J O G A R   |
                                                                                            ◣————————————————————◢""" + Style.RESET_ALL )
    print(Style.BRIGHT + Fore.RED + r"""
                                                                                            ◤————————————————————◥ 
                                                                                            |     2. S A I R     |
                                                                                            ◣————————————————————◢""" + Style.RESET_ALL )
    print("\n>>  ", end="")
    jogar = input()
    
    

    if jogar == "1":
        return True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')    
        exit()
    
       

menu()
os.system('cls' if os.name == 'nt' else 'clear')    


def narracao_intro():
    narrativa = [Style.BRIGHT + Fore.LIGHTWHITE_EX +
        "\nNas terras esquecidas de Eltherra, onde os reinos vivem à sombra dos deuses," 
        "nasceu uma chama de esperança: Lumina, a Deusa da Luz. "

        "\nCom sua luz pura, ela selou os horrores da escuridão e trouxe séculos de paz."

        "\nMas das profundezas do vazio, ergueu-se Varkas — o Lorde das Sombras. "
        "Um ser corrompido por ambição, banido por Lumina por desafiar sua ordem sagrada."

        "\nVarkas convocou os antigos espectros, mergulhando o mundo em trevas e caos."
        "Cidades arderam. Reinos tombaram. E a guerra se iniciou."

        "\nAgora, cabe aos heróis empunhar a luz de Lumina mais uma vez... " 
        "E destruir Varkas antes que a escuridão consuma tudo."

        "\n☼ Escolha seu destino... ou pereça na sombra."+ Style.RESET_ALL
     ] 
    
    for linha in narrativa:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)
        
narracao_intro()
input (Style.BRIGHT + Fore.YELLOW + "\n[ P R E S S  E N T E R ]" + Style.RESET_ALL )
os.system('cls' if os.name == 'nt' else 'clear')


def narracao1():
    
    narrativa1 = [Style.BRIGHT + Fore.LIGHTWHITE_EX +
        f"Kael é o Vigia da Brumia.",
        "Seu corpo, uma sombra do que era, agora é um eco de dor e solidão.",
        "Mas dentro dele, uma centelha de esperança ainda brilha."+ Style.RESET_ALL]
    
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

    narrativa2 = [Style.BRIGHT + Fore.LIGHTWHITE_EX +
        f"Você deve fazer que Kael reuna os fragmentos da Espada Estelar e restaurar o equilíbrio em Aurora.",
        "\nMas cuidado...",
        "\nA escuridão não é apenas uma força externa. Ela também habita dentro de nós.",
        "E as escolhas podem ser mais difícil do que parece."+ Style.RESET_ALL]
    
    for linha in narrativa2:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(4)
narracao2()
input (Style.BRIGHT + Fore.YELLOW + "\n[ P R E S S  E N T E R ]" + Style.RESET_ALL )
os.system('cls' if os.name == 'nt' else 'clear')


