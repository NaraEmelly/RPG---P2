class Item:
    def __init__(self, name, description, effect=None):
        self.name = name
        self.description = description
        self.effect = effect
        
    def use(self, player):
        if self.effect:
            self.effect(player)

# Example items
def heal_player(player):
    player.health += 10
    print(f"{player.name} has been healed by 10 points!")

health_potion = Item("Health Potion", "A potion that restores health.", heal_player)
sword = Item("Sword", "A sharp blade for combat.")
key = Item("Key", "A key that unlocks a door.")