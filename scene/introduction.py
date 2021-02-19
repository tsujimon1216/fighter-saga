from monster import *
from story import enemies


def introduction(story):
    name = input("あなたの名前を教えてください: ")
    ally = Ally(name, 150, 50, 20)
    enemy = enemies[story][0]
    ally.print_status()
    enemy.print_status()
    print()
    return ally, enemy
