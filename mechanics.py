import time
import os
from entities import *
from eldensoul import *


def StartBattle():
    player1 = MainHeroEasy
    player2 = EvilDog
    Battle()

def Battle(player1, player2):
    while (player1.hp or player2.hp > 0):
        print("Choose an action to perform!")
        print("Attack    Parry    Evade    UseMagic")
        selection = input()
        if input == "Attack":
            AttackP1()
        elif input == "Parry":
            ParryP1()
        elif input == "Evade":
            EvadeP1()
        elif input == "UseMagic":
            UseMagicP1()
        






def AttackP1(player1, player2):
    player2.hp = player1.attack / player2.armor

def ParryP1():
    # if p2 uses atk will stun the opponent and he won't be able to move in his next turn (2 moves straight)
    print()

def EvadeP1():
    # makes you evade a non parryable attack
    print()

def UseMagicP1():
    # makes you use magic if you have spells
    print()
    
def AttackP2(player1, player2):
    player1.hp = player2.attack / player1.armor