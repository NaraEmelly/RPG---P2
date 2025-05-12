import random
import time
import os
import sys
from player import Player  


def cena_1():
    print("||||| Cena 1: O Despertar |||||")
    narrador = [
        "\nVocê acorda caído em um ambiente escuro e sujo. Aparentemente parece ser um templo em ruínas.",
        "Em sua frente você vê um pergaminho no chão, e ao lado dele um chicote de couro com uma assinatura estranha.",
        "Você se levanta..."
    ]
    
    for linha in narrador:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)

# Inventário simples
item_escolhido = None

def escolhas_1():
    global item_escolhido

    print(f"\nVocê: O que aconteceu comigo? Me sinto estranho...")

    print("\nVocê vê um chicote e um pergaminho no chão. Escolha abaixo:")
    print("1. Pegar o chicote e seguir em frente.")
    print("2. Pegar o pergaminho.")
    print("3. Ignorar ambos e seguir em frente.")
    
    escolha = input("\n>> ").strip()

    if escolha == "1":
        item_escolhido = "chicote"
        print("\nVocê pega o chicote e sente algo estranho... é como se já soubesse como usá-lo.")
    elif escolha == "2":
        item_escolhido = "pergaminho"
        print("\nVocê pega o pergaminho e lê:")
        print(f'"VOCÊ É A ESPERANÇA DO NOSSO POVO. NÃO SEJA SEDUZIDO PELAS SOMBRAS."')
    elif escolha == "3":
        item_escolhido = "nada"
        print("\nVocê ignora ambos e segue em frente, mas sente que algo está errado...")
        print("Você olha em sua volta e vê uma escultura intacta.")
    else:
        print("\nEscolha inválida. Tente novamente.\n")
        return escolhas_1()
    
    for linha in escolha:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)
    print("\n( Você escuta uma voz sussurrando em sua mente, mas não consegue entender o que ela diz. )")
    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')
    

def cena_2():
    
    print("|||||  Corredor  |||||")
    print("\nVocê avança por um corredor estreito do templo... o som de água pingando ecoa pelas paredes.")
    time.sleep(2)

    if item_escolhido == "chicote":
        print("\nUma armadilha é acionada! Flechas disparam das paredes!")
        print("Com reflexos rápidos, você usa o chicote para puxar uma pedra e se proteger.")
        print(f"Você: Uau... como eu soube fazer isso?")
    elif item_escolhido == "pergaminho":
        print("\nVocê sente um calor vindo do peito... o pergaminho brilha e desintegra no ar.")
        print("As runas no chão brilham e desativam uma armadilha que estava prestes a disparar.")
        print(f"Você: Esse artefato... ele me protegeu!")
    elif item_escolhido == "nada":
        print("\nVocê pisa em uma pedra solta... *CLACK!*")
        print("Uma chuva de flechas é disparada! Você se joga no chão, mas uma delas te acerta.")
        print(f"Você: Maldição! Eu devia ter pegado alguma coisa...")

    for linha in cena_2:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(4)
    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')


def escolhas_2():
    print("\nVocê segue mancando e sangrando até uma porta antiga...")
    
    print(r"""    
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|||||||||||||_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|||||||||||||1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|||||| ||||||_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|||||| ||||||p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|||||||||||||_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|||||||||||||r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_||o-_||||||||_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|||||||||||||l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|||||||||||||_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|||||||||||||n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|||||||||||||_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]============[@] \|  `. | `._  |   `-._ 88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888888888888
""")
    
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')
    # continuar daqui com escolhas_2() e depois cena_3()

#isso são para iniciar o jogo:

cena_1()
escolhas_1()
cena_2()
escolhas_2()

def cena_3():
    
    print("||||| Sala do Trono |||||")
    print("\nVocê chega a uma sala grande, cheia de estátuas antigas e uma sensação de opressão no ar.")
    time.sleep(2)

    if item_escolhido == "chicote":
        print("\nEnquanto você avança, você vê uma figura misteriosa à distância. Antes que possa reagir, a figura ativa uma armadilha!")
        print("Com um movimento rápido, você usa o chicote para desarmar o dispositivo e alcançar a figura.")
        print(f"Você: Algo me diz que estou ficando mais habilidoso com isso... mas quem é essa figura?")
    elif item_escolhido == "pergaminho":
        print("\nAo entrar, as runas nas paredes começam a brilhar. O pergaminho que você carrega brilha com força, sugerindo que você deve usá-lo.")
        print("As runas começam a formar palavras e você entende que essa sala guarda uma chave para o próximo passo em sua jornada.")
        print(f"Você: Eu preciso decifrar isso para avançar!")
    elif item_escolhido == "nada":
        print("\nVocê avança, mas o peso de sua escolha se faz sentir. Um ser sombrio se aproxima rapidamente!")
        print("Você se vê cercado e não há nada que possa fazer para se defender. O confronto parece inevitável.")
        print(f"Você: Eu devia ter me preparado melhor...")

    for linha in cena_3:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(4)
    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')



def escolhas_3():
    print("Você está diante de uma grande porta ornamentada. Dentro, você sente uma presença intensa.")
    print("\nO que você deseja fazer?")
    print("1. Abrir a porta e enfrentar o que está atrás dela.")
    print("2. Procurar por outra saída no ambiente.")
    print("3. Voltar para o corredor e tentar encontrar uma pista no templo.")
    
    escolha = input("\n>> ").strip()
    
    if escolha == "1":
        print("\nVocê abre a porta e se prepara para o que vem a seguir. O destino aguarda.")
        # Aqui pode chamar outra função para a continuação da história
    elif escolha == "2":
        print("\nVocê explora os cantos da sala e encontra uma passagem secreta que te leva a uma nova área.")
    elif escolha == "3":
        print("\nVocê volta para o corredor, determinado a procurar mais pistas que possam te ajudar.")
    else:
        print("\nEscolha inválida. Tente novamente.")
        return 
    
    for linha in escolhas_3:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(4)

        cena_3()
        escolhas_3()
