import random


def make_rand_num():
    return random.randint(1, 9)


def questions():
    num1 = make_rand_num()
    num2 = make_rand_num()
    return num1, num2, num1 * num2


def check_the_answer():
    question = questions()
    print(str(question[0]) + " × " + str(question[1]) + " = ?")
    if int(input("answer = ")) == question[2]:
        return True
    else:
        return False
