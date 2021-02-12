import random


def make_rand_num():
    return random.randint(1,9)


def questions():
    questions_answer = make_rand_num()*make_rand_num()
    return questions_answer


def check_the_answer():
    input_answer = input('input_answer : ')
    if questions() == int(input_answer):
        return True
    else:
        return False


