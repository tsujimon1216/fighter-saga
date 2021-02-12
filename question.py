import random


def make_rand_num():
    return random.randint(1, 9)


class Question:
    def __init__(self):
        self.num1 = make_rand_num()
        self.num2 = make_rand_num()
        self.ans = self.num1 * self.num2

    def check_the_answer(self):
        print(str(self.num1) + " × " + str(self.num2) + " = ?")
        if int(input("answer = ")) == self.ans:
            return True
        else:
            return False
