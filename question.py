import random


def make_rand_num(digits):
    return random.randint(1, (10 ** digits) - 1)


class Question:
    def __init__(self, digits=1):
        self.num1 = make_rand_num(digits)
        self.num2 = make_rand_num(digits)
        self.ans = self.num1 * self.num2

    def check_the_multiplication(self):
        print("10秒以内に答えよ")
        print(str(self.num1) + " × " + str(self.num2) + " = ?")
        input_answer = int(input("answer = "))
        if input_answer == self.ans:
            return True
        else:
            return False

    def check_the_division(self):
        print("10秒以内に答えよ")
        print(str(self.ans) + " ÷ " + str(self.num1) + " = ?")
        input_answer = int(input("answer = "))
        if input_answer == self.num2:
            return True
        else:
            return False
