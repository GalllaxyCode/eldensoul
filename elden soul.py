import time
import os

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

diff = ["Easy", "Normal", "Hard", "Impossible"]
Difficulty = diff[2]
gameclass = ["wretch"]
Class = gameclass[0]
finalbossentitylist = ["Morgott, The Omen King", "Godfrey, First Elden Lord", "Maliketh, The Black Blade", "Malenia, Blade Of Miquella"]

def Settings():
    diff = ["Easy", "Normal", "Hard", "Impossible"]
    Difficulty = diff[2]
    gameclass = ["wretch"]
    Class = gameclass[0]
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print(f"Difficulty = {Difficulty}\nClass = {Class}")
    input("Press Enter to return...")
    SelectGameMode()

def FinalBoss():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(4)
    print("So you reached your peak, tarnished...")
    time.sleep(2)
    print("are you sure you can become the new LORD?")
    time.sleep(2)
    print("I'll test you right now, the last test")
    time.sleep(2)
    if Difficulty == diff[1]:
        print("I AM GODFREY, THE FIRST ELDEN LORD")
        time.sleep(1)
        print(f"\nPrepare to fight {finalbossentitylist[1]}!")
    elif Difficulty == diff[2]:
        print(f"I'm {finalbossentitylist[2]}")
        time.sleep(1)
        print(f"\nPrepare to fight {finalbossentitylist[2]}!")

game_start()