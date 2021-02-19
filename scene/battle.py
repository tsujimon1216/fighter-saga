from question import Question


def battle(ally, enemy, level):
    flag = True
    while ally.hp > 0 and enemy.hp > 0:
        question = Question(level)
        while flag:
            print()
            command = input("1...attack / 2...recover = ")
            if command.isdigit() and command == "1":
                ally.attack_to_enemy(enemy, question)
                break
            elif command.isdigit() and command == "2":
                ally.hp_recovery(question)
                break
        print()
        if enemy.hp <= 0:
            return ally
        enemy.attack_to_ally(ally)
        if ally.hp <= 0:
            return enemy
