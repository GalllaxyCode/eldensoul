import time
import os
from entities import *
from mechanics import *

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
MainHeroNormal = Entity(130, 4, 27, 0, 0)
MainHeroHard = Entity(120, 3, 22, 0, 0)
MainHeroImpossible = Entity(100, 2, 18, 0, 0)
EvilDog = Entity(50, 0, 15, 0, 15)
MorgottTheOmenKing = Entity(300, 10, 70, 20, 20)