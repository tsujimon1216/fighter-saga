def select_level(level):
    while 1:
        play_level = input('select level\\1...easy 2..normal 3..hard :')
        if play_level.isdigit() and (play_level == "1" or play_level == "2" or play_level == "3"):
            level[0] = int(play_level)
            break
        else:
            print("Not Applicable")