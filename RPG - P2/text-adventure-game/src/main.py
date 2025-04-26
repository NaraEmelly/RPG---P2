# filepath: text-adventure-game/text-adventure-game/src/main.py

import sys
from cenas.intro import start_intro
from pontuação.tracker import ScoreTracker

def main():
    print("Bem-vindo ao Jogo de Crie o seu futuro!")
    score_tracker = ScoreTracker()
    
    while True:
        start_intro(score_tracker)
        choice = input("Deseja jogar novamente? (s/n): ").lower()
        if choice != 's':
            print("Obrigado por jogar!")
        else:
            exit()
            
if __name__ == "__main__":
    main()