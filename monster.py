# coding=utf-8
class Monster:
    def __init__(self, monster_id, name, life_point, attack_point, defence_point):
        self.monster_id = monster_id
        self.name = name
        self.life_point = life_point
        self.attack_point = attack_point
        self.defence_point = defence_point

    def get_monster_id(self):
        return self.monster_id

    def get_name(self):
        return self.name

    def get_life_point(self):
        return self.life_point

    def get_attack_point(self):
        return self.attack_point

    def get_defence_point(self):
        return self.defence_point

    def change_life_point(self, dif):
        self.life_point += dif

    def attack_to(self, the_other, is_collect):
        if is_collect:
            damage = the_other.defence_point - self.attack_point
            the_other.change_life_point(damage)
            print(self.get_name() + "の攻撃！")
            print(the_other.get_name() + "に" + str(-damage) + "ダメージ！")
            print(the_other.get_name() + "の体力は残り" + str(the_other.get_life_point()))
        else:
            print(self.get_name() + "の攻撃ははずれた！")
