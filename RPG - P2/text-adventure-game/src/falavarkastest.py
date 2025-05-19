import time
import os
import sys
import colorama 
from colorama import Fore, Back, Style


def Varkas():
  Varkas = [ Style.BRIGHT + Fore.RED + 
              "Dizem que fui consumido pelas Sombras… Mas não contam o que a Luz me fez.",
            "\nHá muito tempo, no reino de Aurora, eu era apenas um jovem cavaleiro, respeitado e amado pelo povo.",
           "Treinado desde a infância pelos meus pais, aprendi a proteger os inocentes e a seguir os preceitos da Ordem da Luz.",
           "Fui fiel. Leal. Um guardião daquilo que chamavam de sagrado."
           "\nMeus feitos ecoavam pelas comunidades, e por isso fui convidado a me unir à Ordem.",
            "Mas o mundo não recompensa os bons — ele os devora." 
            "\nEm uma missão para recuperar o mapa da Espada da Luz, fui traído.",
            "Os próprios soldados do reino, temendo minha ascensão, emboscaram meu pelotão.",
            "Vi todos os meus irmãos morrerem… e sobrevivi apenas para ser acusado de traí-los." 
            "\nRetornei ferido, arrastando meu corpo em busca de justiça,",
           "apenas para ser humilhado diante do povo…",
           "Expulso. Julgado. Marcado como traidor.",
           "A deusa Lumina… ela viu a verdade.",
           "Sabia que eu não era o culpado — mas ao invés de me libertar,",
           "lançou-me às masmorras para que a mentira continuasse reinando.",
           "\nLá, nas trevas profundas, eu renasci.",
           "\nCriei um grupo… os Antiluminos",
           "Guerreiros que como eu, haviam sido quebrados pela falsa luz.",
            "Mas fomos caçados. Massacrados como feras.",
            "Eu vi a “luz” que eles pregavam… e era feita de tortura, ódio e silêncio.",
            "\nFoi ali que meu verdadeiro poder despertou.",
            "Queimei vilas. Derrubei templos. Fiz o mundo ouvir meu nome com temor.",
           "Varkas, o Arauto da Escuridão.",
           "Agora, eu não luto mais por justiça… mas por reconstrução.",
           "Irei tomar a Espada da Luz, corrompê-la e moldar com ela um novo mundo.",
           "\nE dessa vez… não haverá Lumina para esconder a verdade."+ Style.RESET_ALL
          ]

  for linha in Varkas:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.010)
        print()
        time.sleep(0.010)  
        
Varkas()
input (Style.BRIGHT + Fore.YELLOW + "\n[ P R E S S  E N T E R ]" + Style.RESET_ALL )
os.system('cls' if os.name == 'nt' else 'clear')


#def historia_varkas():    # outra versão
   # varkas = [Style.BRIGHT + Fore.LIGHTWHITE_EX +
   #  "Há muito tempo atras, no reino de Aurora,",
   #    "um jovem cavaleiro chamado Varkas convivia com os habitantes e era respeitado por todos.",
   #    "Desde pequeno, Varkas foi treinado pelos seus pais para proteger os inocentes,", 
   # "seguindo os preceitos da Ordem da Luz, um grupo sagrado de guardiões que defendia o reino de ameaças mágicas e monstruosas da escuridão.",
   # "Com o passar dos anos, Varkas reconhecido pelos seus feitos nas comunidades, foi chamado para participar da Ordem da Luz,",
   # "tendo mais reconhecimento na sociedade,", 
   #     "mas a verdade é que o mundo nem sempre recompensa os bons.",
    #    "Durante uma missão para recuperar o mapa da espada da luz,",
   #     "Varkas e seu pelotão foram traídos pelos soldados do reino que temia o crescimento de seu poder e popularidade.", 
   #     "A emboscada matou todos os seus companheiros.",
   #    "Varkas sobreviveu, gravemente ferido, apenas para ser acusado de traição ao retornar.",
   #     "Humilhado publicamente, expulso da Ordem e rejeitado por aqueles que um dia o adoraram,", 
   #     "Varkas foi julgado por ter matado todos do pelotão,",
   #     "porem, Lumina viu a escuridão manipulando ele e o deixou sair ileso, por ter visto que ele não os matou,",
    #    "mas o jogou nas masmorras do reino,",
     #   "quando Varkas saiu, com seu ódio criou um grupo de ANTILUMINOS para fazer uma rebelião,",
    #    "contudo, seu grupo foi capturado, massacrado, torturado e morto pelos guardas imperiais da luz,",
    #    "fazendo ele ficar com um extremo ódio ascendente em seu peito,", 
    #    "despertando assim seu grandioso poder da escuridão e traindo completamente a luz,",  
    #    "com seu poder divino, ele destruiu vilas, templos e matou famílias e cidadãos inocentes,",
    #    "percebendo o quão forte ele era,",
    #    "decidiu se tornar um líder da escuridão e criar o seu império",
     #   "e agora ele deseja buscar a espada da luz para converte-la em trevas e criar um novo mundo"+ Style.RESET_ALL
   # ]
  