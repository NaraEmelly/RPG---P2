import random
import time
import os
import sys


def cena_1():
    print("||||| Cena 1: O Despertar |||||")
    narrador = [
        "\nKael acorda caído em um ambiente escuro e sujo. Aparentemente parece ser um templo em ruínas.",
        "Em sua frente você vê um pergaminho no chão, e ao lado dele um chicote de couro com uma escrita antiga.",
        "Ele se levanta..."
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

    print("\nEle vê um chicote e um pergaminho no chão. Escolha abaixo:")
    print("1. Pegar o chicote e seguir em frente.")
    print("2. Pegar o pergaminho.")
    print("3. Ignorar ambos e seguir em frente.")
    
    escolha = input("\n>> ").strip()

    if escolha == "1":
        item_escolhido = "chicote"
        print("\nEle pega o chicote e sente algo estranho... é como se já soubesse como usá-lo.")
    elif escolha == "2":
        item_escolhido = "pergaminho"
        print("\nEle pega o pergaminho e lê:")
        print(f"VOCÊ É A ESPERANÇA DO NOSSO POVO. NÃO SEJA SEDUZIDO PELAS SOMBRAS.")
    elif escolha == "3":
        item_escolhido = "nada"
        print("\nEle ignora ambos e segue em frente, mas sente que algo está errado...")
        
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
    print("\n( Kael escuta uma voz sussurrando em sua mente, mas não consegue entender o que ela diz. )")
    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')
    

def cena_2():
    global item_escolhido
    
    print("|||||  CENA 2: O CORREDOR |||||")
    print("\nKael avança por um corredor estreito do templo... o som de vácuo ecoa pelas paredes.")
    time.sleep(2)

    if item_escolhido == "chicote":
        print("\nUma armadilha é acionada! Flechas disparam das paredes!")
        #Adicionar art de flechas
        print("Com reflexos rápidos, ele usa o chicote para puxar uma pedra e se proteger.")
        print(f"\nKael: Uau... como eu soube fazer isso?! ")
    elif item_escolhido == "pergaminho":
        print("\nEle sente um calor vindo do peito... o pergaminho brilha e desintegra no ar como pó.")
        print("As runas no chão brilham e desativam uma armadilha que estava prestes a disparar.")
        print(f"\nKael: Esse artefato... ele me salvou, UFA!")
    elif item_escolhido == "nada":
        print("\nKael pisa em uma pedra solta... *CLACK!*")
        print("Uma chuva de flechas é disparada! Ele se joga no chão, mas uma delas te acerta.")
        print(f"\nKael: Maldição!! Eu devia ter pegado alguma coisa, talvez evitaria isso...")

    
        print()
        time.sleep(4)
    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')


def escolhas_2():
    print("\nEle segue mancando por um corredor e sangrando até uma porta antiga no final...")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    # continuar daqui com escolhas_2() e depois cena_3()

#isso são para iniciar o jogo:

cena_1()
escolhas_1()
cena_2()
escolhas_2()
 
 #cena_3 removida



def cena_3(): # tambem é a escolha 3
    global item_escolhido
    print("||||| CENA 3: O QUE SERÁ? ONDE DARÁ? |||||")
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

    print("\nVocê está diante de uma grande porta ornamentada. Dentro, você sente uma presença intensa.")
    print("\nO que você deseja fazer?")
    print("\n1. Abrir a porta e enfrentar o que está atrás dela.")
    print("2. Voltar pelo corredor e tentar encontrar uma pista no templo explorando.")
    
    escolha = input("\n>> ").strip()
    
    if escolha == "1":
        print("\nVocê abre a porta e se assusta com os morcegos que sai de dentro dessa sala.",  
        "É apenas um lugar abandonado e destruido.")
        
        print(r"""                                                                                                                                                                                                                                           
                                                                                                       ██                            
                        █   █         █████                                                              █████████                    
                        █████    ██████████████                                                            █████████  █ █               
            █████████████████████████████████████████                                                         ███████ █████            
          ██████████████████████████████████████                                                                   █████████             
        ███████████████████████████████                                                                          ████████████       
      █████████████      ██████                                                                                   ██████████████      
     █                      █ █                                                                                  █ █       ████████     
                                                                                                                                ████    
                                                                                                                                    █""")
        print("\n KAEL: Estranho, por onde eles conseguiram entrar? PRECISO ACHAR A SAÍDA!!")
        
    elif escolha == "2":
        print("||||| CORREDOR |||||")
        print("\nVocê explora o templo e percebe uma estatua meio medonha de mais de 6m de altura.",
        "De alguma forma te dar calafrios.")
        #art estatua por aqui
        print("\nKael: AAH SENTIR UM CALAFRIO O QUE SERÁ ESSA ESTÁTUA? ME SINTO OBSERVADO.")

    elif escolha == "3":
        print("\nKael: EII ONDE QUE VOCÊS ENTRARAM AMIGOS?!!")
        print("\nMorcegos: BRWUIZ w^º^W ...")
        print("\nKael: EU NÃO FALO EM MORCEGÊS :/")

    else:
        print("\nEscolha inválida. Tente novamente.")
        return 
    
    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')

def escolhas_3():
    global item_escolhido
    
    print("Kael precisa encontrar respostas ou pistas para sair desse templo, ele pode a qualquer momento desabar ou algo pior!... ")

    print("\nEscolha o que Kael pode fazer:")
    print("\n1. Analisar as escrituras nas paredes ")
    print("2. Voltar e explorar o templo atrás de pistas")

    escolha = input("\n>> ").strip()

    if escolha == "1":
        print(" Ao observar em detalhes na parede do Templo, Kael notou algo estranho, parecia que a pessoa que fez os desenhos estava apressada",
        " Não estava perfeitamente desenhada, como templos comum, que a cada detalhe deveria está simetricamentre perfeito  ")
        print("\nKael: HuM Parece que uma estátua esconde alguma coisa, é difícil decifrar..")
        print("\n( KAEL OLHA PARA TRÁS E SENTE COMO SE ESTIVESSE SENDO OBSERVADO )")
        print("\n( ELE OLHA PARA CIMA )")
        #aqui deve tá a art da estátua
        print("\nKael: AAAHR~ Que susto! Não tinha notado essa estátua enorme. Uau parece ter mais de 10m...")

    elif escolha == "2":
        print("~~ VOLTANDO PELO CORREDOR ~~")
        print("\nVocê explora o templo e percebe uma estatua meio medonha de mais de 10m de altura.",
        "De alguma forma te dar calafrios.")

        #art estatua por aqui

        print("\nKael: Aah SENTIR UM CALAFRIO O QUE SERÁ ESSA ESTÁTUA? ME SINTO OBSERVADO.")


    else:
        print("\nEscolha inválida. Tente novamente.")
        return 

    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')


cena_3()
escolhas_3()

def cena_4():
    global item_escolhido

    print ("||||| CENA 4: SAIA SE PUDER |||||")

    print("\n")
    print("\n1. ")
    print("2. ")
    print("3. ")

    #terminar

    escolha = input("\n>> ").strip()

    if escolha == "1":
        print("")

    elif escolha == "2":
        print("")

    elif escolha == "2":
        print("")

    # ADICIONAR O CAMINHO DAS ESCOLHAS

    else:
        print("\nEscolha inválida. Tente novamente.")
        return

    time.sleep(2)
    input("\nPRESSIONE ENTER PARA CONTINUAR...")
    os.system('cls' if os.name == 'nt' else 'clear')


def escolhas_4():
    global item_escolhido

    print()

