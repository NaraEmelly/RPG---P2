class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def speak(self):
        return f"{self.name} says: {self.dialogue}"

    def interact(self):
        print(self.speak())
        # Additional interaction logic can be added here

# Example NPCs
def create_npcs():
    npc1 = NPC("Elder", "Welcome, brave adventurer! Your journey begins here.")
    npc2 = NPC("Merchant", "I have the finest goods for sale!")
    return [npc1, npc2]