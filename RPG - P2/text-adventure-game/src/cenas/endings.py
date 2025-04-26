class Endings:
    def __init__(self):
        self.endings = {
            "good": "Você conseguiu salvar o reino e trouxe paz a todos!",
            "bad": "Você falhou em sua missão e o reino caiu em desgraça.",
            "neutral": "Você fez algumas escolhas questionáveis e o destino do reino permanece incerto."
        }

    def display_ending(self, choice):
        if choice in self.endings:
            return self.endings[choice]
        else:
            return "Escolha inválida. O destino do seu personagem permanece em aberto."