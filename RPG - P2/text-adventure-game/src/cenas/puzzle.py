class Puzzle:
    def __init__(self):
        self.solved = False

    def display_puzzle(self):
        print("Você se depara com um enigma:")
        print("O que é que quanto mais se tira, maior fica?")
        print("1. Buraco")
        print("2. Sombra")
        print("3. Tempo")

    def check_answer(self, answer):
        if answer == "1":
            self.solved = True
            print("Você resolveu o enigma! O caminho está livre.")
        else:
            print("Resposta errada. Tente novamente.")

    def is_solved(self):
        return self.solved

def main():
    puzzle = Puzzle()
    while not puzzle.is_solved():
        puzzle.display_puzzle()
        answer = input("Digite o número da sua resposta: ")
        puzzle.check_answer(answer)

if __name__ == "__main__":
    main()