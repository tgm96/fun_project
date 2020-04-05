import random
import monsters
import time
import math

def selector(move):
    if move == "stab":
        select = random.randint(1, 100)
        if select in range(1, 81):
            return "hit"
        else:
            return "miss"
    
    if move == "slash":
        select = random.randint(1, 100)
        if select in range(1, 61):
            return "hit"
        else:
            return "miss"

class Player:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.moves = ["stab", "slash", "use potion"]
        self.potions = 3
        self.stunned = False
        self.has_armour = False
        self.has_shield = False
        self.armour_value = 0
        self.shield_value = 0


    def choose(self):
        time.sleep(1)
        print("-----------------------------------------------------")
        choice = input("Make a move, " + " / ".join(self.moves) + 
        ": 1/2/3 \n\n")
        return choice

    def welcome_player(self):
        print("Welcome, " + self.name)
        print("\nYou have three moves: ")
        print("\nStab: a fast and sharp move that almost never " +
        "misses, but it deals little damage")
        print("\nSlash: a powerful strike that deals a lot of damage" + 
        " but it is slow and may miss")
        print("\nUse potion: it gives your body new strength, but you only have three\n\n")
        time.sleep(0.5)

    def use_potion(self):
        if self.potions == 0:
            time.sleep(1)
            print("You are out of potions!\n")
        else:
            time.sleep(1)
            self.potions -= 1
            heal = random.randint(20, 41)
            self.hp += heal
            print("\nyou drink the potion and heal with " +
                str(heal) + " hp\n")

    def display_hp(self):
        if self.has_armour == True and self.armour_value > 0:
            print("you now have " + str(self.armour_value) + " armour points")

        if self.has_shield == True and self.shield_value > 0:
            print("you now have " + str(self.shield_value) + " shield points")
        
        print("you now have " + str(self.hp) + " hp\n")

    def update_hp(self, damage):
        a = math.ceil((damage / 100) * 20)
        if self.has_armour == True and self.armour_value > 0:
            self.armour_value -= a
        else:
            self.hp -= damage

    def update_armour(self, damage):
        a = math.ceil((damage / 100) * 20)
        if self.has_armour == True and self.armour_value > 0:
            self.armour_value -= a

    def update_shield(self, damage):
        a = math.ceil((damage / 100) * 60)
        if self.has_shield and self.shield_value > 0:
            self.shield_value -= a
    
    def attack(self, choice):
        # make the player attack!
        if choice == "1":
            result = selector("stab")
            if result == "hit":
                damage = random.randint(20, 30)
                time.sleep(1)
                if self.stunned == True:
                    damage -= 20
                    print("You are STUNNED from the roar, and deal less damage")
                print("\nYou stab the monster. It deals " + str(damage) + " damage\n")
                return damage
            else:
                time.sleep(1)
                print("\nYou stab at the monster, it dodges your blade\n")
        elif choice == "2":
            result = selector("slash")
            if result == "hit":
                damage = random.randint(30, 40)
                time.sleep(1)
                if self.stunned == True:
                    damage -= 10
                    print("You are STUNNED from the roar, and deal less damage")
                print("\nYou slash the monster. It deals " + str(damage) + " damage\n")
                return damage
            else:
                time.sleep(1)
                print("\nYour slash is too slow and the monster jumps away\n")
    
    def block(self=None):
        block = input("Do you wish to block the attack? y/n: ")
        if block == "y":
            return True
        else:
            return False


    
