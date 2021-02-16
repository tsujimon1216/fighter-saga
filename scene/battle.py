from question import Question


def battle(ally, enemy, result):
    flag = True
    while ally.hp > 0 and enemy.hp > 0:
        question = Question()
        while flag:
            command = input("1...attack / 2...recover = ")
            if command.isdigit() and command == "1":
                ally.attack_to_enemy(enemy, question)
                break
            elif command.isdigit() and command == "2":
                ally.hp_recovery(question)
                break
        if enemy.hp <= 0:
            result[0] = ally
            break
        print("")
        enemy.attack_to_ally(ally)
        if ally.hp <= 0:
            result[0] = enemy
            break
