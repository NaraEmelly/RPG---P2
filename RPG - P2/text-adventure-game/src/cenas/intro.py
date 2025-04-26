# This file contains the introduction scene of the text adventure game.

def intro_scene():
    print("Bem-vindo ao mundo de Aventura Épica!")
    print("Você é um herói em busca de glória e tesouros.")
    print("Sua jornada começa em uma pequena aldeia, onde rumores de um dragão aterrorizando a região têm circulado.")
    print("Você deve decidir como proceder.")
    
    print("\nEscolha uma opção:")
    print("1. Visitar a taverna para coletar informações.")
    print("2. Ir diretamente para a caverna do dragão.")
    print("3. Explorar a floresta em busca de aliados.")
    
    choice = input("Digite o número da sua escolha: ")
    
    return choice