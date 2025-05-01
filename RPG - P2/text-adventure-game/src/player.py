



player = {
    'nome': "Kael",
    'level': 1,
    'exp': 0,
    'exp_max': 50,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,
    'corrupcao': 0,  # Novo atributo para rastrear a corrupção
    'corrupcao_max': 100,  # Limite máximo de corrupção
}

def aumentar_corrupcao(jogador, quantidade):
    jogador['corrupcao'] += quantidade
    if jogador['corrupcao'] >= jogador['corrupcao_max']:
        print(f"{jogador['nome']} foi consumido pelas sombras!")
        # Aqui é para implementar o final sombrio do jogo (final ruim)
        # Podemos adicionar lógica para encerrar o jogo ou recomeçar 

