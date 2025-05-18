import random
import time
import os
import sys
import colorama
from colorama import Fore, Back, Style
from intro import menu, narracao_intro, historia_varkas, narracao1, narracao2
from escolhas import cena_1, escolhas_1, cena_2, escolhas_2, cena_3, escolhas_3, cena_4, escolhas_4



def main():
    

    # Chama a função de menu do arquivo intro.py
    menu()
    os.system('cls' if os.name == 'nt' else 'clear')

    # Chama a função de narração do arquivo intro.py
    narracao_intro()
    os.system('cls' if os.name == 'nt' else 'clear')

    historia_varkas()
    os.system('cls' if os.name == 'nt' else 'clear')

    narracao1()
    os.system('cls' if os.name == 'nt' else 'clear')

    # Inicia a primeira cena
    cena_1()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas_1()
    os.system('cls' if os.name == 'nt' else 'clear')

    cena_2()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas_2()
    os.system('cls' if os.name == 'nt' else 'clear')

    cena_3()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas_3()
    os.system('cls' if os.name == 'nt' else 'clear')

    cena_4()
    os.system('cls' if os.name == 'nt' else 'clear')

    escolhas_4()
    os.system('cls' if os.name == 'nt' else 'clear')
    


if __name__ == "__main__":
    main()
