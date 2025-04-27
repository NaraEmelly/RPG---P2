import random
import time
import os
import sys
import cmd

class Player: # atributo do jogador
    def __init__(self):
        self.nome = "Kael"
        self.classe = "Guerreiro da Névoa"
        self.força = 7
        self.agilidade = 5
        self.resistencia = 6
        self.inteligencia = 4
        self.fe_luz = 3
        self.corrupcao_trevas = 0 # Vai aumentando conforme o jogador faz escolhas sombrias
        self.vida = 100
        

    def __str__(self):
        return f"Nome: {self.nome}, Classe: {self.classe}, Força: {self.força}, Agilidade: {self.agilidade}, Resistência: {self.resistencia}, Inteligência: {self.inteligencia}, Fé na Luz: {self.fe_luz}, Corrupção das Trevas: {self.corrupcao_trevas}, Vida: {self.vida}"

    