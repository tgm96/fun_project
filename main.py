import monsters
import conditions
import time
from player import Player
import fights
import choices


player_name = input("Enter your name: ")

player = Player(player_name)
time.sleep(0.2)
player.welcome_player()

while True:
    """
    fights.fight_brute(player)
    if player.hp < 1:
        break
    bum = choices.doors()

    choices.results(bum, player)

    print("You leave the room and go back to the hallway.\n")
    choices.results("R", player)

    fights.fight_dragon(player)
    if player.hp < 1:
        break
    """
    choices.bodies(player)
    
    fights.fight_skeleton(player)
    if player.hp < 1:
        break

    bum = choices.doors()
    choices.results(bum, player)

