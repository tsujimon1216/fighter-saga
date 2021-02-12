def start_scene():
    print("                ========================================")
    print("                =                                      =")
    print("                =      ~~~~   fighter game   ~~~~      =")
    print("                =                                      =")
    print("                ========================================")


def select_play_level():
    while 0:
        play_level = input('                  level select\\1...easy 2..normal 3..hard :')
        if play_level.isdecimal() and (play_level == 1 or play_level == 2 or play_level == 3):
            return play_level

        else:
            print("                error")
