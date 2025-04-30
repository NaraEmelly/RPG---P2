import os
import sys          
import time
import random
import cmd



def cena_acordar_caverna():
    narrativa2 = [
        "Um som do vazio ecoa pela escuridão...",
        "Você desperta, os olhos ainda pesados, em meio ao caos da escuridão.",
        "Correntes frias apertam seus pulsos, prendendo-o às pedras ásperas da caverna.",
        "O ar cheira a umidade e decadência, e o som distante de gotas d'água ressoa como tambores de solidão.",
        "Seus instintos gritam: VOCÊ PRECISA SE LIBERTAR !!!.",
        "Mas a quem pertence esta caverna? E o que te aguarda além dela?",
    ]
    
    for linha in narrativa2:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)


time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
cena_acordar_caverna()

