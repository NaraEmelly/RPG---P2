import cmd
import sys

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


class PlayerCommand(cmd.Cmd):  # Comandos do jogador
    intro = "Bem-vindo ao jogo! Digite 'ajuda' para ver os comandos disponíveis."
    prompt = "--> "
    intro = input()

    def __init__(self, player):
        super().__init__()
        self.player = player

    def do_ver_status(self, arg):
        """Exibe o status do jogador."""
        print(self.player)

    def do_ver_itens(self, arg):
        """Exibe os itens do jogador."""
        print(f"Itens: {', '.join(self.player.itens)}")

    def do_usar_item(self, item):
        """Usa um item do inventário. Exemplo: usar_item Poção de Vida"""
        if item in self.player.itens:
            if item == "Poção de Vida":
                self.player.hp += 10
                self.player.itens.remove(item)
                print("Você usou uma Poção de Vida: +10 HP")
            elif item == "Chicote de Sangue":
                print("Você usou o Chicote de Sangue: -15 HP do inimigo")
                self.player.itens.remove(item)
            else:
                print(f"O item {item} não pode ser usado.")
        else:
            print(f"Item {item} não encontrado no inventário.")

    def do_sair(self, arg):
        """Sai do jogo."""
        print("Saindo do jogo. Até a próxima!")
        return True


if __name__ == "__main__":
    player = Player()
    player_command = PlayerCommand(player)
    player_command.cmdloop()
    

