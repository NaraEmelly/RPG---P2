import cmd
import sy

class Player:  # Atributo do jogador
    def __init__(self):
        self.nome = "Kael"
        self.classe = "Guerreiro da Névoa"
        self.força = 7
        self.agilidade = 5
        self.resistencia = 6
        self.inteligencia = 4
        self.fe_luz = 3
        self.corrupcao_trevas = 0  # Vai aumentando conforme o jogador faz escolhas sombrias
        self.hp = 100
        self.itens = ["Chicote de Sangue", "Poção de Vida"]
        

    def __str__(self):
        return (
            f"Nome: {self.nome}, Classe: {self.classe}, Força: {self.força}, "
            f"Agilidade: {self.agilidade}, Resistência: {self.resistencia}, "
            f"Inteligência: {self.inteligencia}, Fé na Luz: {self.fe_luz}, "
            f"Corrupção das Trevas: {self.corrupcao_trevas}, Vida: {self.hp}"
        )




