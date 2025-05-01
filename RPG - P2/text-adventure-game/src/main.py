# filepath: text-adventure-game/text-adventure-game/src/main.py
#arquivo principal do jogo
# importando as bibliotecas necessárias
import random   
import time
import cmd
import os
import sys
import intro
import player
import npcs
import puzzle
import capitulos
import escolhas
import criaturas

# Adicionando o caminho do diretório src ao sys.path para importar módulos corretamente
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Importando outros módulos necessários do projeto

# Inicializando o jogo
if __name__ == "__main__":
    intro.show_intro()
    game_logic.start_game()

