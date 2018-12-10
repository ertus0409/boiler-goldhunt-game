#
# CS 177 - project2.py
# Ertugrul Ucar - PUID:0031006019
# This program constructs a "Boiler Gold Hunt" game which creates a window with
#   many black circles. The player can click on one of many black circles and reveal
#   the hidden colors under them. The challange is to find the only gold colored circle
#   with the least clicks. ENJOY!
#

# Importing graphics library
from graphics import *
# Importing random to choose the place of golden circle
import random


# GAME CONTROL  ===========================================================================
def gameControl():
    # Initial setup of Game Control window
    gameControl = GraphWin("Game Control", 250, 200)
    gameControl.setBackground("light grey")
    # Additional objects inside the window:
    #Header
    header = Rectangle(Point(0,0),Point(250,35))
    header.setFill("black")
    header.draw(gameControl)
    #Title - Boiler Gold Hunt
    title = Text(header.getCenter(), "BOILER GOLD HUNT!")
    title.setTextColor("gold")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(gameControl)
    #SubTitle - Player Name
    subTitle = Text(Point(125,80), "PLAYER NAME :")
    subTitle.draw(gameControl)
    #Name Entry Field
    nameFld = Entry(Point(125, 105), 20)
    nameFld.draw(gameControl)
    nameFld.setFill("white")
    #Exit Button and Exit Label
    exitBtn = Rectangle(Point(240,190), Point(160,160))
    exitBtn.setFill("black")
    exitLbl = Text(exitBtn.getCenter(), "EXIT")
    exitLbl.setTextColor("white")
    exitBtn.draw(gameControl)
    exitLbl.draw(gameControl)
    #NewGame Button and NewGame Label
    newGameBtn = Rectangle(Point(10,190), Point(90,160))
    newGameBtn.setFill("gold")
    newGameLbl = Text(newGameBtn.getCenter(), "NEW GAME")
    newGameLbl.setTextColor("black")
    newGameBtn.draw(gameControl)
    newGameLbl.draw(gameControl)
    return [nameFld, newGameBtn, exitBtn, gameControl]





# GAME WINDOW   =====================================================================================
def gameWindow():
    # Initial setup for Game Window
    gameWin = GraphWin("GoldHunt", 480, 520)
    #Additional objects inside the window:
    #Header
    header = Rectangle(Point(0,0), Point(480,40))
    header.setFill("black")
    header.draw(gameWin)
    #Rounds Label
    rounds = Text(Point(40,20), "Round: 0")
    rounds.setTextColor("gold")
    rounds.draw(gameWin)
    #Clicks Label
    clicks = Text(Point(440,20), "Clicks: 0")
    clicks.setTextColor("gold")
    clicks.draw(gameWin)
    return [rounds, clicks, gameWin]



# STARTING THE GAME FUNCTIONALITIES  =================================================================
def gameStart(gameWin, playerName):
    # Overriding the same name text object if it exists; else
    #   a name object is created
    try:
        name.setText("Player: {}".format(playerName))
    except:
        # PlayerName Text
        name = Text(Point(240,20), "Player: {}".format(playerName))
        name.setFill("gold")
        name.draw(gameWin)


    # To store all the created circles
    circles = []
    #Initial Point
    xi = 25
    yi = 65
    inc = 30
    #Initial Point Circle Test:
    for i in range(15):
        y = yi+(inc*i)
        for z in range(15):
            x = xi+(inc*z)
            circle = Circle(Point(x,y),15)
            circle.setFill("black")
            circles.append(circle)
            circle.draw(gameWin)
    # Using Random Class to choose the gold circle
    goldi = random.randint(0, len(circles)-1)
    # Assigning colors
    colors = ["white"]*225
    for i in range(225):
        #Distance calculation
        distance = calculateDistance(circles[i].getCenter(), circles[goldi].getCenter())
        #Grey circles calculation
        if ((30 * (2**(1/2))) < distance <= (60 * (2**(1/2)))):
            colors[i] = "grey"
        #Tan circles calculation
        elif (distance <= (30 * (2**(1/2)))):
            colors[i] = "tan"
        #Gold circle
        if (i == goldi):
            colors[i] = "gold"
    return [circles, colors]





# MAIN FUNCTION ==========================================================================================
def main():
    #Description
    print("This program constructs a Boiler Gold Hunt game which creates a window with\n many black circles. The player can click on one of many black circles and reveal\n the hidden colors under them. The challange is to find the only gold colored circle\n with the least clicks. ENJOY!")
    # Calling gameWindow() and gameControl() and assaigning return objects
    gc = gameControl()
    gw = gameWindow()
    nameFld = gc[0]
    newGameBtn = gc[1] #PointOne(10,190), PointTwo(90,160)
    exitBtn = gc[2] #PointOne(240,190), PointTwo(160,160)
    controlWin = gc[3] #250x200
    roundText = gw[0]
    clickText = gw[1]
    gameWin = gw[2] #480x520
    clickCount = 0
    gameOn = True
    name = ""
    # The game continues until an exit button is escaped
    while gameOn:
        # Checking for mouse clicks
        controlClick = controlWin.checkMouse()
        if (controlClick != None):
            # Exit Condition:
            if (240 > controlClick.getX() > 160) and (190 > controlClick.getY() > 160) :
                #Closing the windows
                gameWin.close()
                controlWin.close()
                gameOn = False
            # NewGame Condition:
            elif (90 > controlClick.getX() > 10) and (190 > controlClick.getY() > 160):
                # Username check
                if nameFld.getText().strip() == "":
                    # Error messae
                    errorMsg = Text(Point(125, 135), "Please Enter A Username")
                    errorMsg.setStyle("bold")
                    errorMsg.setTextColor("red")
                    errorMsg.draw(controlWin)
                else:
                    #Disappearing error message if it exists
                    if "errorMsg" in locals():
                        errorMsg.setText("")
                    #Game Starts
                    roundCount = 0
                    while (roundCount <= 5):
                        #New round
                        name = nameFld.getText()
                        gs = gameStart(gameWin, nameFld.getText())
                        #Necessary variables stored outside their loops for later use
                        circles = gs[0]
                        colors = gs[1]
                        inRound = True
                        goldenIndex = 0
                        #Round begins
                        while inRound:
                            # Checking for control window
                            controlClick = controlWin.checkMouse()
                            if (controlClick != None):
                                # Exit Condition:
                                if (240 > controlClick.getX() > 160) and (190 > controlClick.getY() > 160) :
                                    #Closing the windows
                                    gameWin.close()
                                    controlWin.close()
                                    break
                                # New Game Condition
                                elif (90 > controlClick.getX() > 10) and (190 > controlClick.getY() > 160):
                                    gameWin.close()
                                    controlWin.close()
                                    main()
                            gameClick = gameWin.checkMouse()
                            if (gameClick != None):
                                #Updating click count
                                clickCount += 1
                                clickText.setText("Clicks: {}".format(clickCount))
                                for i in range(225):
                                    if (calculateDistance(circles[i].getCenter(), gameClick) <= 15):
                                        circles[i].setFill(colors[i])
                                        # If the golden ball is found
                                        if (colors[i] == "gold"):
                                            #Storing the index of goldi to remove it later on
                                            goldenIndex = i
                                            #Animating the balls as if they are falling (In order to
                                            #   experience the animation the computer running the script
                                            #   should run it fast)
                                            while (circles[0].getCenter().getY() <= 550):
                                                for item in circles:
                                                    # Checking for control window
                                                    controlClick = controlWin.checkMouse()
                                                    if (controlClick != None):
                                                        # Exit Condition:
                                                        if (240 > controlClick.getX() > 160) and (190 > controlClick.getY() > 160) :
                                                            #Closing the windows
                                                            gameWin.close()
                                                            controlWin.close()
                                                            gameOn = False
                                                            break
                                                        # New Game Condition
                                                        elif (90 > controlClick.getX() > 10) and (190 > controlClick.getY() > 160):
                                                            gameWin.close()
                                                            controlWin.close()
                                                            main()
                                                    if (item.config["fill"] != "gold"):
                                                        #item.move(0,30)
                                                        item.move(0,1080)
                                            inRound = False
                        #Incrementing round number
                        roundCount += 1
                        roundText.setText("Round: {}".format(roundCount))
                        print(roundCount)
                        #Disappearing gold ball
                        circles[goldenIndex].undraw()
                        #Message indicating the end of the round
                        finText = Text(Point(240,260), "Click To Continue To The Next Round!")
                        finText.draw(gameWin)
                        gameWin.getMouse()
                        finText.undraw()
                    #Creating scores.txt
                    try:
                        fileScores = open("scores.txt","r+")
                    except:
                        fileScores = open("scores.txt","w+")
                    rawList = fileScores.readlines()
                    rawList.append("{},{}\n".format(name,clickCount))
                    print(rawList)
                    rawList.sort(key=secondkey)
                    print(rawList)
                    fileScores.truncate(0)
                    for item in rawList:
                        fileScores.write(item)
                    fileScores.close()
                    gameOn = False

#For the purpose of ordering scores.txt
def secondkey(myList):
    l = myList.split(",")
    return l[1]









# Calculating distance between Point objects ================================================
def calculateDistance(pOne, pTwo):
    #Performing Pythagoras
    a = pOne.getX() - pTwo.getX()
    b = pOne.getY() - pTwo.getY()
    return ((a**2)+(b**2))**(1/2)




main()
