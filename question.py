import random
import time


def make_rand_num():
    return random.randint(1, 9)


class Question:
    def __init__(self):
        self.num1 = make_rand_num()
        self.num2 = make_rand_num()
        self.ans = self.num1 * self.num2
        self.elapsed_time = 0

    def check_the_multiplication(self):
        self.elapsed_time = 0
        start = time.time()
        print("10秒以内に答えよ")
        print(str(self.num1) + " × " + str(self.num2) + " = ?")
        input_answer = int(input("answer = "))
        end = time.time()
        self.elapsed_time = int(end - start)
        if input_answer == self.ans and self.elapsed_time <= 10:
            return True
        else:
            return False

    def get_elapsed_time(self):
        return self.elapsed_time

    def check_the_division(self):
        self.elapsed_time = 0
        start = time.time()
        print("10秒以内に答えよ")
        print(str(self.ans) + " ÷ " + str(self.num1) + " = ?")
        input_answer = int(input("answer = "))
        end = time.time()
        self.elapsed_time = int(end - start)
        if input_answer == self.num2 and self.elapsed_time <= 10:
            return True
        else:
            return False
