import time
import os
from entities import *
from mechanics import *

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

def game_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print("▄▀▀█▄▄▄▄  ▄▀▀▀▀▄     ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄      ▄▀▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄     \n▐  ▄▀   ▐ █    █     █ ▄▀   █ ▐  ▄▀   ▐ █  █ █ █     █ █   ▐ █      █ █   █    █ █    █      \n  █▄▄▄▄▄  ▐    █     ▐ █    █   █▄▄▄▄▄  ▐  █  ▀█        ▀▄   █      █ ▐  █    █  ▐    █      \n  █    ▌      █        █    █   █    ▌    █   █      ▀▄   █  ▀▄    ▄▀   █    █       █       \n ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄▀  ▄▀▄▄▄▄   ▄▀   █        █▀▀▀     ▀▀▀▀      ▀▄▄▄▄▀    ▄▀▄▄▄▄▄▄▀ \n █    ▐     █        █     ▐   █    ▐   █    ▐        ▐                            █         \n ▐          ▐        ▐         ▐        ▐                                          ▐         ")
    time.sleep(3)
    print("WELCOME TO THE GAME, TARNISHED. It's time for another challenge...")
    time.sleep(3)
    print("Are you ready?")
    SelectGameMode()

def SelectGameMode():
    time.sleep(1)
    print("\nSelect the gamemode:")
    time.sleep(1)
    print("Story    FinalBoss    Settings    Credits")
    while(True):
        selection = input()
        if selection == "Story":
            Story()
        elif selection == "FinalBoss":
            FinalBoss()
        elif selection == "Settings":
            Settings()
        elif selection == "Credits":
            Credits()
        else:
            time.sleep(2)
            print("Wrong input, try again")


def Credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(3)
    GalllaxyCode = link('https://github.com/GalllaxyCode', "GalllaxyCode")
    print(f"Every single line of code was created by {GalllaxyCode}")
    input("Press Enter to return...")
    SelectGameMode()

class SettingsClass():
    diff = ["Easy", "Normal", "Hard", "Impossible"]
    Difficulty = diff[3]
    gameclass = ["wretch"]
    Class = gameclass[0]
    finalbossentitylist = ["Morgott, The Omen King", "Godfrey, First Elden Lord", "Maliketh, The Black Blade", "Malenia, Blade Of Miquella"]
    def __init__(self, difficulty, mode):
        self.Difficulty = difficulty
        self.Class = mode

p1 = SettingsClass("Impossible", "wretch")

def Settings():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print(f"Difficulty = {p1.Difficulty}\nClass = {p1.Class}")
    time.sleep(1)
    print("\nType setting you want to change...")
    select = input()
    if select == "Difficulty":
        DifficultyChange()
    elif select == "Class":
        ClassChange()
    SelectGameMode()

def DifficultyChange():
    print("Select and write on of these:")
    print(SettingsClass.diff)
    selectDifficulty = input()
    if selectDifficulty == "Easy":
        p1.__init__(SettingsClass.diff[0], p1.Class)
    elif selectDifficulty == "Normal":
        p1.__init__(SettingsClass.diff[1], p1.Class)
    elif selectDifficulty == "Hard":
        p1.__init__(SettingsClass.diff[2], p1.Class)
    elif selectDifficulty == "Impossible":
        p1.__init__(SettingsClass.diff[3], p1.Class)
    else:
        print("Wrong input, try again.")
    Settings()

def ClassChange():
    print("This option is under development!")
    time.sleep(2)
    Settings()

def FinalBoss():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(4)
    print("So you reached your peak, tarnished...")
    time.sleep(2)
    print("are you sure you can become the new LORD?")
    time.sleep(2)
    print("I'll test you right now, the last test")
    time.sleep(2)
    if p1.Difficulty == "Easy":
        print(f"I'm {SettingsClass.finalbossentitylist[0]}")
        time.sleep(1)
        print('\nHave it writ upon thy meagre grave:\n"Felled by King Morgott! Last of all kings."')
        time.sleep(1)
        print(f"\nPrepare to fight {SettingsClass.finalbossentitylist[0]}!")
    elif p1.Difficulty == "Normal":
        print("I'm {SettingsClass.finalbossentitylist[1]}")
        time.sleep(1)
        print(f"\nPrepare to fight {SettingsClass.finalbossentitylist[1]}!")
    elif p1.Difficulty == "Hard":
        print(f"I'm {SettingsClass.finalbossentitylist[2]}")
        time.sleep(1)
        print("Cower before Maliketh, Marika’s Black Blade")
        time.sleep(1)
        print(f"\nPrepare to fight {SettingsClass.finalbossentitylist[2]}!")
    elif p1.Difficulty == "Impossible":
        print(f"\nI'm {SettingsClass.finalbossentitylist[3]}")
        time.sleep(1)
        print("\nAnd i have never known defeat")
        time.sleep(1)
        print(f"\nPrepare to fight {SettingsClass.finalbossentitylist[3]}!")

def Story():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nThe erd tree...")
    time.sleep(2)
    print("\nthe most powerful source of energy in this world")
    time.sleep(2)
    print("\nis now...")
    time.sleep(3)
    print("   ________  ______  _____ __________ \n  / ____/ / / / __ \/ ___// ____/ __ \\\n / /   / / / / /_/ /\__ \/ __/ / / / /\n/ /___/ /_/ / _, _/___/ / /___/ /_/ / \n\____/\____/_/ |_|/____/_____/_____/  \n                                      ")
    time.sleep(2)
    print("The Evil Dog is invading you!")
    time.sleep(1)
    print("Prepare to fight!")
    StartBattle()

game_start()