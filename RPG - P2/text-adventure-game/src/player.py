import os
import time



class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_max = 50
        self.hp = 100
        self.hp_max = 100
        self.dano = 25
        self.corrupcao = 0  # Novo atributo para rastrear a corrupção
        self.corrupcao_max = 100  # Limite máximo de corrupção

    def aumentar_corrupcao(self, quantidade):
        self.corrupcao += quantidade
        if self.corrupcao >= self.corrupcao_max:
            print(f"{self.name} foi consumido pelas sombras!")
            # Aqui é para implementar o final sombrio do jogo (final ruim)
            # Podemos adicionar lógica para encerrar o jogo ou recomeçar

    def mostrar_status(self):
        print(f"Nome: {self.name}")
        print(f"Nível: {self.level}")
        print(f"Experiência: {self.exp}/{self.exp_max}")
        print(f"HP: {self.hp}/{self.hp_max}")
        print(f"Dano: {self.dano}")
        print(f"Corrupção: {self.corrupcao}/{self.corrupcao_max}")

    def equipar (self, item):
        if item == "chicote":
            self.dano += 10
            print(f"{self.name} equipou o chicote! Dano aumentado para {self.dano}.")
        elif item == "pergaminho":
            self.hp += 20
            print(f"{self.name} usou o pergaminho! HP aumentado para {self.hp}.")
        else:
            print("Item desconhecido.")

    def comandos(self):
        print("Comandos disponíveis:")
        print("1. Mostrar status")
        print("2. Equipar item")
        print("3. Sair")

def main():
    player = Player(name)
    while True:
        player.comandos()
        comando = input("Escolha um comando: ")
        if comando == "1":
            player.mostrar_status()
        elif comando == "2":
            item = input("Escolha um item para equipar (chicote/pergaminho): ")
            player.equipar(item)
        elif comando == "3":
            print("Saindo do jogo...")
            break
        else:
            print("Comando inválido. Tente novamente.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Limpa a tela após cada comando
        # Adiciona uma pausa para o jogador ler a mensagem