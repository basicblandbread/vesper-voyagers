class Player:
    def __init__(self, name, hp=100, attack=10, defense=5, speed=5):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount): 
        self.hp = max(0, self.hp - amount)
    
    def __str__(self):
        return f"{self.name} | HP: {self.hp} | ATK: {self.attack} | DEF: {self.defense} | SPD: {self.speed}"
    
if __name__ == '__main__':
    p = Player('Aria')
    print(p)
    p.take_damage(30)
    print(p)
    p.take_damage(999)
    print(f'Alive? {p.is_alive()}')
