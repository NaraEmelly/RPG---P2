# filepath: text-adventure-game/text-adventure-game/src/main.py
#arquivo principal do jogo

import random   
import time
import cmd
import os
import sys
import intro
import escolhas

main = True
while main:
    
    
   
    
    
    # Chama a função de menu do arquivo intro.py
    intro.menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Chama a função de narração do arquivo intro.py
    intro.narracao_intro()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Chama a função de narração do arquivo escolhas.py
    escolhas.cena_1()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas.escolhas_1()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas.cena_2()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas.escolhas_2()
    os.system('cls' if os.name == 'nt' else 'clear')



    
    

