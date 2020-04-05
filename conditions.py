import monsters
import player
import time

def update_stats(player_hp, monster_hp):
    if player_hp < 1:
        print("the monster has bested you and the world fades to darkness...")
        time.sleep(2)
        print("a light appears far away...")
        time.sleep(2)
        print("in the light, a silhouette of a person...")
        time.sleep(2)
        print("the person says:")
        time.sleep(3)
        print("'get recked'")
        time.sleep(3)
        print("THE END! YOU LOST!")

    
    if monster_hp < 1:
        print("you have bested the monster and it is dead\n")
        time.sleep(2)
        print("the blood spreads in a pool on the cobbles.\n")
        time.sleep(1.5)
        print("...\n")
        time.sleep(4)
        
        