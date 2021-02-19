# coding=utf-8
import random


class Monster:
    def __init__(self, name, hp, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.max_hp = hp
        self.origin_attack = attack
        self.origin_defence = defence

    def print_status(self):
        print(self.name, "\nHP:", self.hp, "\nAtk:", self.attack, "\nDef:", self.defence)

    def change_hp(self, dif):
        self.hp += dif


class Enemy(Monster):
    def attack_to_ally(self, ally):
        attack_random = random.randint(1, 3)
        if attack_random == 1 or attack_random == 2:
            damage = ally.defence - self.attack
            ally.change_hp(damage)
            print(self.name + "の攻撃！")
            print(ally.name + "に" + str(-damage) + "ダメージ！")
            if ally.hp <= 0:
                print(ally.name + "の体力は残り0\n")
            else:
                print(ally.name + "の体力は残り" + str(ally.hp) + "\n")
        elif attack_random == 3:
            print(self.name + "の攻撃ははずれた！\n")

    def change_enemy_monster(self):
        self.max_hp += 50
        self.hp = self.max_hp
        self.attack += 20
        self.defence += 15
        print("next_monster...")


class Ally(Monster):

    def attack_to_enemy(self, enemy, question):
        if question.check_the_multiplication():
            if self.hp < self.max_hp * 0.3 and self.attack != self.origin_attack * 1.5:
                self.attack = self.attack * 1.5
                print("攻撃力が1.5倍になった。")
            elif self.hp > self.max_hp * 0.3 and self.attack == self.origin_attack * 1.5:
                self.attack = self.origin_attack
                print("攻撃力が元に戻った。")

            damage = enemy.defence - self.attack
            enemy.change_hp(damage)
            print(self.name + "の攻撃！")
            print(enemy.name + "に" + str(-damage) + "ダメージ！")
            if enemy.hp <= 0:
                print(enemy.name + "の体力は残り0\n")
            else:
                print(enemy.name + "の体力は残り" + str(enemy.hp) + "\n")
        else:
            if question.get_elapsed_time() <= 10:
                print(self.name + "の攻撃ははずれた！\n")
            else:
                print("時間オーバーです。\n")

    def hp_recovery(self, question):
        if question.check_the_division():
            if self.hp > 100:
                self.hp = self.max_hp
                print(self.name + "の体力は満タンになった!")
            else:
                self.change_hp(50)
                print(self.name + "は体力を50回復した")
        else:
            if question.get_elapsed_time() > 10:
                print("時間オーバーです。\n")
            else:
                print(self.name + "は体力を回復できなかった\n")

    def status_up(self):
        self.attack += 10
        self.origin_attack += 10
        self.max_hp += 50
        self.defence += 10
        print("")
        print(self.name + "のステータスが上がった")
        print(self.name + "のMAX_HPは50上がった")
        print(self.name + "の攻撃力は10上がった")
        print(self.name + "の防御力は10上がった")
        print("")
