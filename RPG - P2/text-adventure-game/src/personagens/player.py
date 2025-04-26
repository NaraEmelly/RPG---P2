class Player:
    def __init__(self, Matias):
        self.name = Matias
        self.health = 100
        self.max_health = 100
        self.attack_power = 10
        self.defense = 5
        self.level = 1
        self.experience = 10
        self.experience_to_next_level = 100
        self.inventory_capacity = 10
        self.inventory_weigth = 0
        self.inventory = []


    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def attack(self):
        return self.attack_power
    
    def level_up(self):
        if self.experience >= self.experience_to_next_level:
            self.level += 1
            self.esperience -= self.experience_to_next_level
            self.experience_to_next_level *= 2
            self.max_health += 10
            self.attack_power += 5
            self.defense += 2
            self.inventory_capacity += 1
            self.inventory_weigth += 1
            self.experience = 0
        else:
            print("Parabéns! Você subiu de nível!")
            print(f"Você agora é nível {self.level}!")
            print(f"Experiência necessária para o próximo nível: {self.experience_to_next_level}")
            print(f"Vida máxima: {self.max_health}")
            print(f"Poder de ataque: {self.attack_power}")
            print(f"Defesa: {self.defense}")
            print(f"Capacidade do inventário: {self.inventory_capacity}")
            print(f"Peso do inventário: {self.inventory_weigth}")
            print(f"Experiência: {self.experience}")

    def add_experience(self, amount):
        self.experience += amount
        if self.experience >= self.experience_to_next_level:
            self.level_up()
            self.experience_to_next_level - self.experience
            self.experience = 0
            self.experience_to_next_level *= 2
            self.max_health += 10
            self.attack_power += 5
            self.defense += 2
            self.inventory_capacity += 1
            self.inventory_weigth += 1
            self.experience = 0
        else:
            print("Experiência adicionada com sucesso!")
            print(f"Experiência atual: {self.experience}")
            print(f"Experiência necessária para o próximo nível: {self.experience_to_next_level}")
            print(f"Vida máxima: {self.max_health}")
            print(f"Poder de ataque: {self.attack_power}")
            print(f"Defesa: {self.defense}")
            print(f"Capacidade do inventário: {self.inventory_capacity}")
            print(f"Peso do inventário: {self.inventory_weigth}")
            print(f"Inventário: {self.inventory}")

    def check_inventory_capacity(self):
        if len(self.inventory) >= self.inventory_capacity:
            print("Inventário cheio! Não é possível adicionar mais itens.")
            return False
        return True
    
    def check_inventory_weight(self):
        total_weight = sum(item.weight for item in self.inventory)
        if total_weight > self.inventory_weigth:
            print("Peso do inventário excedido! Não é possível adicionar mais itens.")
            return False
        return True
        
    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def show_inventory(self):
        return self.inventory

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Player: {self.name}, Health: {self.health}, Inventory: {self.inventory}"
    
    def __repr__(self):
        return f"Player({self.name}, {self.health}, {self.inventory})"
    
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self.health == other.health and self.inventory == other.inventory
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):        
        if isinstance(other, Player):
            return self.level < other.level
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Player):
            return self.level <= other.level
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Player):
            return self.level > other.level
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Player):
            return self.level >= other.level
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Player):
            return Player(self.name + other.name, self.health + other.health)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Player):
            return Player(self.name - other.name, self.health - other.health)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Player):
            return Player(self.name * other.name, self.health * other.health)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, Player):
            return Player(self.name / other.name, self.health / other.health)
        return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, Player):
            return Player(self.name // other.name, self.health // other.health)
        return NotImplemented
    
    def __mod__(self, other):
        if isinstance(other, Player):
            return Player(self.name % other.name, self.health % other.health)
        return NotImplemented
    
    def __pow__(self, other):
        if isinstance(other, Player):
            return Player(self.name ** other.name, self.health ** other.health)
        return NotImplemented
    
    def __and__(self, other):
        if isinstance(other, Player):
            return Player(self.name & other.name, self.health & other.health)
        return NotImplemented
    
    def __or__(self, other):
        if isinstance(other, Player):
            return Player(self.name | other.name, self.health | other.health)
        return NotImplemented
    
    def __xor__(self, other):
        if isinstance(other, Player):
            return Player(self.name ^ other.name, self.health ^ other.health)
        return NotImplemented
    
    def __invert__(self):
        return Player(~self.name, ~self.health)
    
    def __call__(self, *args, **kwargs):
        return self.name(*args, **kwargs)
    
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self, key):
        return self.name[key]
    
    def __setitem__(self, key, value):
        self.name[key] = value

    def __delitem__(self, key):
        del self.name[key]

    def __contains__(self, item):
        return item in self.name
    
    def __iter__(self):
        return iter(self.name)
    
    def __next__(self): 
        return next(self.name)
    
    def __reversed__(self):
        return reversed(self.name)
    
    def __hash__(self): 
        return hash(self.name)
    
    def __bool__(self):
        return bool(self.name)
    
    def __format__(self, format_spec):  
        return format(self.name, format_spec)
    
    def __sizeof__(self):
        return self.name.__sizeof__()
    
    def __dir__(self):
        return dir(self.name)
    
    def __getattr__(self, name):
        return getattr(self.name, name)
    
    def __setattr__(self, name, value):
        setattr(self.name, name, value)

    def __delattr__(self, name):
        delattr(self.name, name)

    def __reduce__(self):
        return self.name.__reduce__()
    
    def __reduce_ex__(self, protocol):
        return self.name.__reduce_ex__(protocol)
    
    def __sizeof__(self):   
        return self.name.__sizeof__()
    
    def __getstate__(self): 
        return self.name.__getstate__()
    
    def __setstate__(self, state):
        self.name.__setstate__(state)