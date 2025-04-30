import random
import time
import os
import sys
import cmd
import textwrap
import re



def menu():
    print('''
██╗░░░░░██╗░░░██╗███████╗  ███████╗  ░██████╗░█████╗░███╗░░██╗░██████╗░██╗░░░██╗███████╗
██║░░░░░██║░░░██║╚════██║  ██╔════╝  ██╔════╝██╔══██╗████╗░██║██╔════╝░██║░░░██║██╔════╝
██║░░░░░██║░░░██║░░███╔═╝  █████╗░░  ╚█████╗░███████║██╔██╗██║██║░░██╗░██║░░░██║█████╗░░
██║░░░░░██║░░░██║██╔══╝░░  ██╔══╝░░  ░╚═══██╗██╔══██║██║╚████║██║░░╚██╗██║░░░██║██╔══╝░░
███████╗╚██████╔╝███████╗  ███████╗  ██████╔╝██║░░██║██║░╚███║╚██████╔╝╚██████╔╝███████╗
╚══════╝░╚═════╝░╚══════╝  ╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚═════╝░╚══════╝''')
    
    print("\n[[[[[1. Jogar]]]]]")
    print("\n[[[[[2. Sair]]]]]")
    print("\n>> Selecione uma opção: ", end="")
    jogar = input()

    if jogar == "1":
        print("\n~~ Jogo iniciado...")
        time.sleep(0.05)

    else:
        print("\n~~ Jogo encerrado...")
        time.sleep(0.05)
        exit()
menu()
os.system('cls' if os.name == 'nt' else 'clear')

 
def narracao_intro():
    narrativa = [
        "Há muito tempo, antes que as estrelas esquecessem seus nomes...",
        "O continente de Aeloria florescia sob o olhar da Deusa Lumina.",
        "A Espada Estelar, forjada pelas mãos dos Filhos da Aurora, mantinha o equilíbrio entre luz e trevas.",
        "Mas a ambição dos homens foi maior que sua fé...",
        "O Lorde Varkas, seduzido pelo sussurro das sombras, traiu a luz e rasgou o véu da eternidade.",
        "Em sua queda, arrastou consigo reinos inteiros, afundando o mundo em eras de escuridão e sangue.",
        "Somente os Vigias da Brumia permaneceram firmes, guardiões silenciosos de uma esperança esquecida.",
        "E agora, enquanto a Noite Eterna se aproxima...",
        "O último dos Vigias desperta de um sono forçado, acorrentado sob as ruínas do Templo da Aurora.",]

    for linha in narrativa:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)

narracao_intro()
os.system('cls' if os.name == 'nt' else 'clear')


print(r"""
                                      A
                                     |\|
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                  ~-[{o}]-~
                                     |/|
                                     |/|
             ///~`     |\\_          `0'         =\\\\         . .
            ,  |='  ,||\_| ~-_                    _|  \      _/_/|
           / ,' ,;((((((    ~ \                  `~~~\-~-_ /~ (_/\
         /' -~/~)))))))'\_   _/'                      \_  /'  D   |
        |       (((((( ~-/ ~-/                          ~-;  /    \--_
         ~~--|   ))''    ')  `                            `~~\_    \   )
             :        (_  ~\           ,                    /~~-     ./
              \        \_   )--__  /(_/)                   |    )    )|
    ___       |_     \__/~-__    ~~   ,'      /,_;,   __--|   _/      |
  //~~\`\    /' ~~~----|     ~~~~~~~~'        \-  ((~~    __-~        |
((()   `\`\_(_     _-~~-\                      ``~~ ~~~~~~   \_      /
 )))     ~----'   /      \                                   )       )
  (         ;`~--'        :                                _-    ,;;(
            |    `\       |                             _-~    ,;;;;)
            |    /'`\     ;                          _-~          _/
           /~   /    |    )                         /;;;''  ,;;:-~
          |    /     / | /                         |;;'   ,''
          /   /     |  \\|                         |   ,;(    
        _/  /'       \  \_)                   .---__\_    \,--._______
       ( )|'         |~-_|                   (;;'  ;;;~~~/' `;;|  `;;;\
        ) `\_         |-_;;--__               ~~~----__/'    /'_______/
        `----'       |   `~--_ ~~~;;------------~~~~~ ;;;'_/'
                     `~~~~~~~~'~~~-----....___;;;____---~~
      """)
    

def narracao1():
    narrativa1 = [
        "Você é Kael, um Vigia da Brumia.",
        "Seu corpo, uma sombra do que era, agora é um eco de dor e solidão.",
        "Mas dentro de você, uma centelha de esperança ainda brilha.",
        "Você deve reunir os fragmentos da Espada Estelar e restaurar o equilíbrio em Aeloria.",
        "Mas cuidado...",
        "A escuridão não é apenas uma força externa. Ela também habita dentro de nós.",
        "E a escolha entre luz e sombra pode ser mais difícil do que parece."
    ]
    
    for linha in narrativa1:
        for caractere in linha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(1.5)  # pausa entre as frases para dar efeito cinematográfico

narracao1()
