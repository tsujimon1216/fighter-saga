from question import Question


def battle(ally, enemy, result):
    while ally.hp > 0 and enemy.hp > 0:
        question = Question()
        ally.attack_to_enemy(enemy, question)
        enemy.attack_to_ally(ally)
        if ally.hp < 0:
            result[0] = enemy
        elif enemy.hp < 0:
            result[0] = ally
