import time
from player import Player
import monsters
import fights


def doors():
    print("You gather yourself after the fight and you start down the dim hallway.\n")
    time.sleep(2)
    player_choice = input("A torch marks the end of the hallway."
    " There are two doors. One to the right, one to the left."
    " Which one do you choose to go through?\nL or R?: ")

    if player_choice.lower() == "r":
        return "R"
    else:
        return "L"

def bodies(player):
    print("you find behind the dragon an old skeleton\n")
    time.sleep(1)
    print("It still has its rusty armour on, and strapped on its arm is a shield\n")
    time.sleep(1)
    print("do you pick up the shield? y/n ")
    choice = input("> ")
    
    if choice.lower() == "y":
        time.sleep(1)
        print("you unstrap the shield and put it on your arm\n")
        time.sleep(1)
        print("you now have a fourth option, to block the enemy's attack, however, the shield will break over time\n")
        player.has_shield = True
        player.shield_value = 100
    
    time.sleep(1)
    print("you step over the skeleton and move on down the hallway")

def results(choice, player):
    if choice == "R":
        print("You open the door on the right. As it opens," + 
            " you feel a wall of heat slam you in the face.\n\n")
        time.sleep(1)
        return "dragon"
    else:
        time.sleep(1)
        print("You carefully walk towards the door, all the while holding your sword ready.\n")
        time.sleep(1.2)
        print("When it's close enough, you grab the handle and push open the door.\n")
        time.sleep(1)
        print("Behind is a small room with a candle on the floor.\n")
        time.sleep(1)
        print("Beside the candle is a chest.\n")
        time.sleep(1)
        open_chest = input("Do you open the chest?\n Y/N: ")
        if open_chest.lower() == "y":
            time.sleep(1)
            print("In the chest your find a set of armour")
            print("This armour gives you 50 armour points,")
            print("and it reduces the damage taken from monsters.\n")
            time.sleep(2)
            player.has_armour = True
            player.armour_value = 50
        else:
            time.sleep(1)
            print("Goodbye cruel world")

