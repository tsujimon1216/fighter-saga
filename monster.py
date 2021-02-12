# coding=utf-8
class Monster:
    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def print_status(self):
        print(self.name, "\nHP:", self.hp, "\nAtk:", self.attack, "\nDef:", self.defence)

    def change_hp(self, dif):
        self.hp += dif


class Enemy(Monster):
    def attack_to_ally(self, ally):
        damage = ally.defence - self.attack
        ally.change_hp(damage)
        print(self.name + "の攻撃！")
        print(ally.name + "に" + str(-damage) + "ダメージ！")
        print(ally.name + "の体力は残り" + str(ally.hp) + "\n")


class Ally(Monster):
    def attack_to_enemy(self, enemy, question):
        if question.check_the_answer():
            damage = enemy.defence - self.attack
            enemy.change_hp(damage)
            print(self.name + "の攻撃！")
            print(enemy.name + "に" + str(-damage) + "ダメージ！")
            print(enemy.name + "の体力は残り" + str(enemy.hp) + "\n")
        else:
            print(self.name + "の攻撃ははずれた！\n")
