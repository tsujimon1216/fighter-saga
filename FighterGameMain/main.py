from monster import *

# from printer import *

# start_scene()
# print(select_play_level())

monster1 = Monster(1, "monster1", 100, 30, 10)
monster2 = Monster(2, "monster2", 200, 60, 20)

while monster1.life_point > 0 and monster2.life_point > 0:
    monster1.attack_to(monster2)
    monster2.attack_to(monster1)
