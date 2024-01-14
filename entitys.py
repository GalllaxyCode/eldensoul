class Entity:
    def __init__(self, hp, armor, atk, spellamp, magresistance):
        self.hp = hp
        self.armor = armor  
        self.atk = atk
        self.spellamp = spellamp
        self.magresistance = magresistance

    def PrintEntityAttributes(self):  
        print(f"I have {self.hp} hp, {self.armor} armor, {self.atk} atk, {self.spellamp} spellamp, {self.magresistance} magic resist")

MainHeroEasy = Entity(150, 5, 33, 5, 0)
MainHeroEasy.PrintEntityAttributes()
