import random
import time


def selector(move):
    if move == "punch":
        select = random.randint(1, 100)
        if select in range(1, 71):
            return "hit"
        else:
            return "miss"
    
    if move == "slash":
        select = random.randint(1, 100)
        if select in range(1, 91):
            return "hit"
        else:
            return "miss"


def run_game():
    player_health = 100
    opp_health = 120

    moves = ["punch", "slash", "heal"]

    heroName = input("What is your name?: ")
    print("Hello " + heroName)
    time.sleep(0.5)
    print("You are fighting a mighty monster. It has 120 points of health\n")
    print("Now you must defeat it\n")
    print("You have three moves: ")
    print("Punch, a powerful strike that deals a lot of damage" + 
        " but it is slow and may miss")
    print("Slash, a fast and sharp move that almost never " +
        "misses, but it deals less damage")
    print("Heal, it gives your body new strength!")

    while True:
        if player_health < 1:
            print("The monster has bested you. You lie on the ground, bleeding.")
            time.sleep(0.5)
            print("The world slowly fades...")
            time.sleep(2)
            print("In the darkness, words form...")
            time.sleep(2)
            print("They say: ")
            time.sleep(3)
            print("'get rekd'")
            break

        print("-----------------\n")
        choice = input("What move will you use? Punch, Slash, or Heal? 1/2/3: ")

        if choice == "2":
            result = selector("slash")
            if result == "hit":
                print("You slash at the monster, cutting its flesh!\n")
                damage = random.randint(10, 21)
                print("It deals " + str(damage) + " damage!\n")
                opp_health -= damage
                if opp_health < 1:
                    print("The monster has 0 health points!\n")
                else:
                    print("The monster has " + str(opp_health) + " health points!\n")
            else:
                print("Your move misses the monster\n")

        elif choice == "1":
            result = selector("punch")
            if result == "hit":
                print("You punch the monster, it staggers backwards!\n")
                damage = random.randint(20, 31)
                print("It deals " + str(damage) + " damage!\n")
                opp_health -= damage
                if opp_health < 1:
                    print("The monster has 0 health points!\n")
                else:
                    print("The monster has " + str(opp_health) + " health points!\n")
            else:
                print("Your punch is slow and the monster dodges!\n")

        elif choice == "3":
            print("You cast a healing spell\n")
            heal = random.randint(10, 30)
            print("It heals you with " + str(heal) + " health points\n")
            player_health += heal
            print("You have " + str(player_health) + " health points\n")
        else:
            print("You have to type the specific move, or else it won't work!\n")

        time.sleep(0.5)

        if opp_health < 1:
            print("The monster is defeated! You search the chest and collect the loot")
            time.sleep(1)
            print("The chest contains a small note...")
            time.sleep(2)
            print("It says: ")
            time.sleep(2)
            print("'hitler did nothing wrong'")
            break

        print("-----------------\n")
        print("The monster makes its move\n")
        
        time.sleep(1)

        monster_choice = moves[random.randint(0,2)]

        if monster_choice == "punch":
            result = selector(monster_choice)
            if result == "hit":
                print("The monster punches you and you almost fall to the floor\n")
                damage = random.randint(20, 30)
                print("The punch deals " + str(damage) + " damage\n")
                player_health -= damage
                if player_health < 1:
                    print("You have 0 health points\n")
                else:
                    print("You have " + str(player_health) + " health points left\n")
            else:
                print("The monster punches slowly, and you slither away from the heavy fist\n")
        
        if monster_choice == "slash":
            result = selector(monster_choice)
            if result == "hit":
                print("The monster slashes at you and it cuts deep\n")
                damage = random.randint(15, 25)
                print("The slash deals " + str(damage) + " damage\n")
                player_health -= damage
                if player_health < 1:
                    print("You have 0 health points\n")
                else:
                    print("You have " + str(player_health) + " health points left\n")
            else:
                print("The monster's slash misses you by a hair\n")
        
        if monster_choice == "heal":
            if opp_health > 120:
                print("The monster keeps its distance, watching\n")
                continue
            print("The monster casts a healing spell\n")
            heal = random.randint(10, 25)
            opp_health += heal
            print("The monster has " + str(opp_health) + " health points left\n")


run_game()