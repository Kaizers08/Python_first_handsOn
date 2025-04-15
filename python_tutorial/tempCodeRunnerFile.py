class Character:
    def __init__(self, character, hp, attack):
        self.character = character
        self.hp = hp
        self.attack = attack
    
    def hps(self):
        print("Your hp life is: " + str(self.hp))
        
    def att(self):
        print("Your Attack Damage is: " + str(self.attack))
        
    def historyOfcharacter(self):
        print("Your Character name is: " + self.character)
        
One = Character("Kaizer", "40HP" , 10, "\n")
One.historyOfcharacter()
One.hps()
One.att()

Two = Character("Jaireell", "80HP", 101, "\n")
Two.historyOfcharacter()
Two.hps()
Two.att()