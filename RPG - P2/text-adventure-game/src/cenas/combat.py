class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_attack(self):
        damage = self.player.attack()
        self.enemy.take_damage(damage)
        print(f"You attack the {self.enemy.name} for {damage} damage!")

    def enemy_attack(self):
        damage = self.enemy.attack()
        self.player.take_damage(damage)
        print(f"The {self.enemy.name} attacks you for {damage} damage!")

    def is_battle_over(self):
        return self.player.is_dead() or self.enemy.is_dead()

    def start_combat(self):
        print(f"A wild {self.enemy.name} appears!")
        while not self.is_battle_over():
            self.player_attack()
            if not self.is_battle_over():
                self.enemy_attack()
        if self.player.is_dead():
            print("You have been defeated!")
        else:
            print(f"You have defeated the {self.enemy.name}!")