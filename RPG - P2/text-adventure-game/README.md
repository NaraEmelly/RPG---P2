# Luz e Sangue 

Este é um jogo de aventura em texto desenvolvido em Python. O jogo permite que os jogadores explorem um mundo interativo, enfrentem desafios, resolvam enigmas e interajam com personagens não-jogáveis (NPCs). As escolhas feitas pelo jogador influenciam o desenrolar da história e podem levar a diferentes finais.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
text-adventure-game
├── src
│   ├── main.py          # Ponto de entrada do jogo
│   ├── cenas           # Módulo que contém as diferentes cenas do jogo
│   │   ├── __init__.py
│   │   ├── intro.py     # Cena de introdução
│   │   ├── combate.py    # Lógica de combate
│   │   ├── puzzle.py     # Lógica de enigmas
│   │   └── finais.py    # Finais do jogo
│   ├── personagens       # Módulo que contém as classes de personagens
│   │   ├── __init__.py
│   │   ├── npc.py       # Classe para NPCs
│   │   └── player.py    # Classe para o jogador
│   ├── inventários        # Módulo que contém a lógica de inventário
│   │   ├── __init__.py
│   │   └── items.py     # Itens do jogo
│   ├── utilitários      # Módulo de utilitários
│   │   ├── __init__.py
│   │   └── helpers.py    # Funções auxiliares
│   └── pontuação        # Módulo de pontuação
│       ├── __init__.py
│       └── tracker.py    # Lógica de rastreamento de pontuação
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
```

## Como Jogar

1. Clone o repositório ou baixe os arquivos do projeto.
2. Instale as dependências necessárias usando o comando:
   ```
   pip install -r requirements.txt
   ```
3. Execute o jogo com o seguinte comando:
   ```
   python src/main.py
   ```
4. Siga as instruções na tela para navegar pelas cenas, interagir com NPCs, resolver enigmas e tomar decisões que afetarão o resultado do jogo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.