def select_story():
    while 1:
        story_id = input('ストーリーを選択\n1...aaa 2..bbb 3..ccc :')
        if story_id.isdigit() and (story_id == "1" or story_id == "2" or story_id == "3"):
            return int(story_id) - 1
        else:
            print("Not Applicable")
