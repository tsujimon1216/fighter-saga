from monster import *
from scene.battle import battle
from scene.introduction import introduction
from scene.select_level import select_level


def start_scene():
    print("========================================")
    print("=                                      =")
    print("=   ~~~~   Fighter Game SAGA   ~~~~    =")
    print("=                                      =")
    print("========================================")


level = {}
result = {}


def select_level_scene():
    select_level(level)


ally = Ally("ally", 150, 50, 20)
enemy = Enemy("enemy", 100, 30, 10)


def intro_scene():
    introduction(ally, enemy)


def battle_scene():
    battle(ally, enemy, result)


def result_scene():
    print("WINNER: " + result[0].name)
