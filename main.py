from scene.start import start
from scene.select_story import select_story
from scene.select_level import select_level
from scene.introduction import introduction
from scene.battle import battle
from scene.result import result

start()
story = select_story()
level = select_level()
enemy_id = 0
ally, enemy = introduction(story)
while ally is not None and enemy is not None:
    enemy_id += 1
    ally, enemy = result(battle(ally, enemy, level), ally, story, enemy_id)
