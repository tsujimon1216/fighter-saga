class ShowGame():
    def StartScene():
        println("                ========================================")
        println("                =                                      =")
        println("                =      ~~~~   fighter game   ~~~~      =")
        println("                =                                      =")
        println("                ========================================")

    def Playlevel():
        while(0):
            PlaylevelNumber = input('                  level select\\1...easy 2..nomal 3..hard :')
            if (PlaylevelNumber.isdecimal() and (PlaylevelNumber == 1 or PlaylevelNumber == 2 or PlaylevelNumber == 3)):
                return PlaylevelNumber
                break
            else:
                println("                error")
