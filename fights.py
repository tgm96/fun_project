from player import Player
import monsters
import conditions
import time
import sys

def fight_brute(player):
    monster = monsters.Brute()
    time.sleep(2)
    monster.descr_monster()
    print()
    while True:
        choice = player.choose()
        if choice == "q":
            sys.exit()
        if choice == "3":
            player.use_potion()
            player.display_hp()
        else:
            pl_dam = player.attack(choice)
            if pl_dam:
                monster.update_hp(pl_dam)
                if monster.hp < 1:
                    conditions.update_stats(player.hp, monster.hp)
                    break
                time.sleep(1)
                print("the monster now has", monster.hp, "hp\n")
        if player.stunned == True:
                player.stunned = False

        move = monster.attack()

        if move["move_type"] == "roar":
            player.update_hp(move["damage"])
            player.stunned = True
        elif move["move_type"] == "hammer":
            player.update_hp(move["damage"])
        elif move["move_type"] == "punch":
            player.update_hp(move["damage"])
        if player.hp < 1:
            conditions.update_stats(player.hp, monster.hp)
            break
        time.sleep(1)
        player.display_hp()

def fight_dragon(player):
    time.sleep(2)
    monster = monsters.Dragon()
    time.sleep(2)
    monster.descr_monster()
    print()

    while True:
        choice = player.choose()
        if choice == "q":
            break
        if choice == "3":
            player.use_potion()
            player.display_hp()
        else:
            pl_dam = player.attack(choice)
            if pl_dam:
                monster.update_hp(pl_dam)
                if monster.hp < 1:
                    conditions.update_stats(player.hp, monster.hp)
                    break
                time.sleep(1)
                print("the monster now has", monster.hp, "hp\n")
        if player.stunned == True:
                player.stunned = False

        move = monster.attack()

        if move["move_type"] == "fire breath":
            player.update_hp(move["damage"])
        elif move["move_type"] == "slash":
            player.update_hp(move["damage"])
        elif move["move_type"] == "tail whip":
            player.update_hp(move["damage"])
        if player.hp < 1:
            conditions.update_stats(player.hp, monster.hp)
            break
        time.sleep(1)
        player.display_hp()

def fight_skeleton(player):
    time.sleep(2)
    monster = monsters.Skeleton()
    time.sleep(2)
    monster.descr_monster()
    print()

    while True:
        choice = player.choose()
        if choice == "q":
            break
        if choice == "3":
            player.use_potion()
            player.display_hp()
        else:
            pl_dam = player.attack(choice)
            if pl_dam:
                monster.update_hp(pl_dam)
                if monster.hp < 1:
                    conditions.update_stats(player.hp, monster.hp)
                    break
                time.sleep(1)
                print("the monster now has", monster.hp, "hp\n")
        if player.stunned == True:
                player.stunned = False

        move = monster.attack(player)

        if move["move_type"] == "stab":
            if move["blocked"] == True:
                player.update_shield(move["damage"])
            else:
                player.update_hp(move["damage"])

        elif move["move_type"] == "slash":
            if move["blocked"] == True:
                player.update_shield(move["damage"])
            else:
                player.update_hp(move["damage"])
                
        #elif move["move_type"] == "block":
            #player.update_hp(move["damage"])
        if player.hp < 1:
            conditions.update_stats(player.hp, monster.hp)
            break
        time.sleep(1)
        player.display_hp()