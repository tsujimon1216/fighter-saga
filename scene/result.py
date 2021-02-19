from story import enemies


def result(winner, ally, story, enemy_id):
    print("WINNER: " + winner.name)
    if winner == ally:
        if enemy_id == len(enemies):
            print("GAME CLEAR")
            return None, None
        else:
            ally.status_up()
            ally.print_status()
            print()
            enemy = enemies[story][enemy_id]
            print("新しい敵があらわれた！")
            enemy.print_status()
            print()
            return ally, enemy
    else:
        print("GAME OVER")
        return None, None
