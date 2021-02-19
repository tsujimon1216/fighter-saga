from scene_manager import *

start_scene()
select_level_scene()
while ally.hp > 0:
    intro_scene()
    battle_scene()
    result_scene()
