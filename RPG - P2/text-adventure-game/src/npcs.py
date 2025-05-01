from random import randint

lista_npcs = []


def criar_npc():
    level = randint(0, 50)

    novo_npc = {
        'nome': f"Inimigo #{level}",
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
    }

    return novo_npc

def gerar_npcs(n_npcs):

    for x in range(n_npcs):
        novo_npc = criar_npc()
        lista_npcs.append(novo_npc)
        # Adiciona o NPC à lista de NPCs
        # Exibe informações do NPC criado
        print(f"NPC {x} criado: {novo_npc['nome']}")
        print(f"Level: {novo_npc['level']}, Dano: {novo_npc['dano']}, HP: {novo_npc['hp']}\n")

def exibir_npcs():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']}, Level: {npc['level']}, Dano: {npc['dano']}, HP: {npc['hp']}"
    )

gerar_npcs(5)

exibir_npcs()

def atacar_npc(npc, player): 
    # Lógica de ataque do jogador ao NPC
    dano_infligido = player['dano'] - npc['dano']
    npc['hp'] -= dano_infligido
    print(f"{player['nome']} atacou {npc['nome']} e causou {dano_infligido} de dano!")
    if npc['hp'] <= 0:
        print(f"{npc['nome']} foi derrotado!")
        lista_npcs.remove(npc)  # Remove o NPC derrotado da lista
    else:
        print(f"{npc['nome']} ainda tem {npc['hp']} HP restante.")

def npc_ataca(npc, player):
    dano_infligido = npc['dano'] - player['dano']
    player['hp'] -= dano_infligido
    print(f"{npc['nome']} atacou {player['nome']} e causou {dano_infligido} de dano!")
    if player['hp'] <= 0:
        print(f"{player['nome']} foi derrotado!")
        # Aqui você pode adicionar lógica para o jogador perder ou reiniciar o jogo
    else:
        print(f"{player['nome']} ainda tem {player['hp']} HP restante.")  

def combate(player, npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc, player)
        if npc['hp'] > 0:  # Verifica se o NPC ainda está vivo antes de atacar
            npc_ataca(npc, player)
    if player['hp'] <= 0:
        print(f"{player['nome']} foi derrotado!")
    elif npc['hp'] <= 0:
        print(f"{npc['nome']} foi derrotado!")
        lista_npcs.remove(npc)



