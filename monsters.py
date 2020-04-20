import random
import time
import player

def selector(move):
    if move == "punch":
        select = random.randint(1, 100)
        if select in range(1, 71):
            return "hit"
        else:
            return "miss"
    
    if move == "hammer":
        select = random.randint(1, 100)
        if select in range(1, 61):
            return "hit"
        else:
            return "miss"
    
    if move == "fire breath":
        select = random.randint(1, 100)
        if select in range(1, 91):
            return "hit"
        else:
            return "miss"
    
    if move == "tail whip":
        select = random.randint(1, 100)
        if select in range(1, 81):
            return "hit"
        else:
            return "miss"
    
    if move == "slash":
        select = random.randint(1, 100)
        if select in range(1, 71):
            return "hit"
        else:
            return "miss"  
    
    if move == "roar":
        select = random.randint(1, 100)
        if select in range(1, 91):
            return "hit"
        else:
            return "miss"

    if move == "stab":
        select = random.randint(1, 100)
        if select in range(1, 91):
            return "hit"
        else:
            return "miss"
    

class Brute():

    def __init__(self):
        self.hp = 10
        self.moves = ["punch", "hammer", "roar"]

    def descr_monster(self):
        print("You face a smelly Brute" 
        " and it has " + str(self.hp) + "hp")
    
    def update_hp(self, pl_dam):
        self.hp -= pl_dam

    def attack(self):
        damage = 0
        choice = random.randint(0, 2)
        time.sleep(1)
        print("the brute uses the move: " + self.moves[choice], "\n")
        if choice == 0:
            result = selector("punch")
            if result == "hit":                
                damage = random.randint(20, 30)
                time.sleep(1)
                print("it deals " + str(damage) + " damage\n")
                return {"damage": damage, "move_type": "punch"}
            else:
                time.sleep(1)
                print("the punch is slow and you dodge the fist\n")
                return {"damage": 0, "move_type": "punch"}
        elif choice == 1:
            result = selector("hammer")
            if result == "hit":        
                damage = random.randint(30, 40)
                time.sleep(1)
                print("it deals " + str(damage) + " damage\n")
                return {"damage": damage, "move_type": "hammer"}
            else:
                time.sleep(1)
                print("the hammer misses your head by a hair\n")
                return {"damage": 0, "move_type": "hammer"}
        elif choice == 2:
            result = selector("roar")
            if result == "hit":
                damage = random.randint(1, 5)
                time.sleep(1)
                print("it deals " + str(damage) + " damage and"
                    + " leaves you stunned in terror\n")
                return {"damage": damage, "move_type": "roar"}
            else:
                time.sleep(1)
                print("The monster coughs and the roar is weak." 
                    + " It leaves you unaffected\n")
                return {"damage": 0, "move_type": "roar"}


class Dragon():

    def __init__(self):
        self.hp = 20
        self.moves = ["fire breath", "slash", "tail whip"]
    
    def descr_monster(self):
        print("This is a mighty Dragon" 
        " and it has " + str(self.hp) + "hp\n")
    
    def update_hp(self, pl_dam):
        self.hp -= pl_dam

    def attack(self):
        damage = 0
        choice = random.randint(0, 2)
        time.sleep(1)
        print("the dragon uses the move: " + self.moves[choice], "\n")
        if choice == 0:
            result = selector("fire breath")
            if result == "hit":                
                damage = random.randint(20, 30)
                time.sleep(1)
                print("it deals " + str(damage) + " damage\n")
                return {"damage": damage, "move_type": "fire breath"}
            else:
                time.sleep(1)
                print("you roll away from the flame\n")
                return {"damage": 0, "move_type": "fire breath"}
        elif choice == 1:
            result = selector("slash")
            if result == "hit":        
                damage = random.randint(30, 40)
                time.sleep(1)
                print("it deals " + str(damage) + " damage\n")
                return {"damage": damage, "move_type": "slash"}
            else:
                time.sleep(1)
                print("the claw misses your head by a hair\n")
                return {"damage": 0, "move_type": "slash"}
        elif choice == 2:
            result = selector("tail whip")
            if result == "hit":
                damage = random.randint(1, 25)
                time.sleep(1)
                print("it deals " + str(damage) + " damage\n")
                return {"damage": damage, "move_type": "tail whip"}
            else:
                time.sleep(1)
                print("The dragon's tail strikes the ground beside you." 
                    + " It leaves you unaffected\n")
                return {"damage": 0, "move_type": "tail whip"}

class Skeleton():

    def __init__(self):
        self.hp = 40
        self.moves = ["stab", "slash", "block"]

    def descr_monster(self):
        print("this is a spooky skeleton armed with a shield and sword")
        print("it has " + str(self.hp) + " hp\n")

    def update_hp(self, pl_dam):
        self.hp -= pl_dam

    def attack(self, player):
        damage = 0
        choice = random.randint(0, 1)
        time.sleep(1)
        print("the skeleton uses the move: " + self.moves[choice]+ "\n")

        if choice == 0:
            result = selector("stab")
            if result == "hit":
                damage = random.randint(15, 25)
                time.sleep(1)

                if player.has_shield:
                    block = player.block()
                    if block:
                        print("you block the stab with your shield\n")
                        return {"damage": damage, "move_type": "stab", "blocked": True}
                    else:
                        print("it deals " + str(damage) + " damage\n")
                        return {"damage": damage, "move_type": "stab", "blocked": False}
                else:
                    print("it deals " + str(damage) + " damage\n")
                    return {"damage": damage, "move_type": "stab", "blocked": False}
            else:
                time.sleep(1)
                print("you step aside from the blade\n")
                return {"damage": 0, "move_type": "stab", "blocked": False}
        
        if choice == 1:
            result = selector("slash")
            if result == "hit":
                damage = random.randint(25, 35)
                time.sleep(1)

                if player.has_shield:
                    block = player.block()
                    if block:
                        print("you block the slash with your shield\n")
                        return {"damage": damage, "move_type": "slash", "blocked": True}
                    else:
                        print("it deals " + str(damage) + " damage\n")
                        return {"damage": damage, "move_type": "stab", "blocked": False}
                else:
                    print("it deals " + str(damage) + " damage\n")
                    return {"damage": damage, "move_type": "stab", "blocked": False}
            else:
                time.sleep(1)
                print("you step aside from the blade\n")
                return {"damage": 0, "move_type": "stab", "blocked": False}
        
        if choice == 2:
            pass