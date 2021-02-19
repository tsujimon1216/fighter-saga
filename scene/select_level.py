def select_level():
    while 1:
        level = input('難易度を選択\n1...easy 2..normal 3..hard :')
        if level.isdigit() and (level == "1" or level == "2" or level == "3"):
            return int(level)
        else:
            print("Not Applicable")