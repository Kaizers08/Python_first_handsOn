"""class Character:
    def __init__(self):
        print("Character Created")
        
charOne = Character()
charTwo = Character()
charThree = Character()"""

class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
    
        
characterOne = Character("Jaireell", 100, 50, 12, 1)
print(characterOne.name)