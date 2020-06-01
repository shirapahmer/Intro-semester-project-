#"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity poicy of the CS department.”

#this is a code to create an interactive game tap tap revolution

import Draw
import random
Draw.setCanvasSize(680,595)
#TO SET UP THE BOARD:

#initialize the lengths of each point of the arrow from the central point (x,y)
flap  = 30  
head  = 40
width = 30
tail  = 60
canvasHeight= 595

#----------------create a function that draws the template for the arrow, facing a given direction and built around one (x,y) point--------------------------------------------

def arrow(x,y,orientation):
                                         
    d = {"left":0, "right":0, "up":0, "down":0}
    if orientation in d:
        d[orientation] += 1
        
    #TO DRAW THE TRIANGLE PART OF THE ARROW: initialize variables to represent the length of the "left flap", "right flap", and "Point" which represent lines of the arrow drawn from the (x,y) reference point
        
    rightFlap = (x + (flap*d["up"])    - (flap*d["down"]) , y + (flap*d["right"]) - (flap*d["left"])) 
    leftFlap = (x - (flap*d["up"])    + (flap*d["down"]) , y - (flap*d["right"]) + (flap*d["left"]))  
    Point  = (x + (head*d["right"]) - (head*d["left"]) , y - (head*d["up"])    + (head*d["down"]))
    coords = [rightFlap,leftFlap,Point]
    Draw.filledPolygon(coords)
    
    #TO DRAW THE RECT PART OF THE ARROW: initialize variables that represent the lines drawn between the distance of the corners of the rect and the (x,y) point  
    
    RI = (x + ((width/2) * d["up"]) - ((width/2) * d["down"]) , y + ((width/2) * d["right"]) - ((width/2) * d["left"]))
    RC = (x +((width/2)*d["up"])-((width/2)*d["down"])-(tail*d["right"])+(tail*d["left"]),\
          y+(tail*d["up"])-(tail * d["down"]) + ((width/2) * d["right"]) - ((width/2) * d["left"]))
    LI = (x - ((width/2) * d["up"]) + ((width/2) * d["down"]) , y - ((width/2) * d["right"]) + ((width/2)*d["left"]))
    LC = (x - ((width/2) * d["up"])+((width/2)*d["down"])-(tail*d["right"])+(tail*d["left"]),\
          y+(tail*d["up"])-(tail*d["down"]) - ((width/2) * d["right"]) + ((width/2) * d["left"]))
    coords = [RI,LI,LC,RC]
    Draw.filledPolygon(coords)
    
#-----------------------------------------draw the score board and lives boxes---------------------------------------------------------------------------------------------------
def setBoard():
    Draw.picture("dancebackground.gif",0,0)
    Draw.picture("dancebackground.gif",295,0)
    Draw.picture("dancebackground.gif",0,148)
    Draw.picture("dancebackground.gif",295,148)
    Draw.picture("dancebackground.gif",0,345)
    Draw.picture("dancebackground.gif",295,345)
    Draw.picture("dancebackground.gif",0,296)
    Draw.picture("dancebackground.gif",295,296)
    Draw.line(500,0,500,190)
    Draw.line(500,190,680,190) 
    Draw.setColor(Draw.BLUE)
    Draw.filledRect(510,30,175,60)
    Draw.filledRect(510,100,175,60)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(30)
    Draw.setFontFamily("Lucida Grande")
    Draw.string("Score:",510,40)
    Draw.string("Lives:",510,110)

    Draw.setColor(Draw.WHITE)  
    arrow(140,80,"left")
    arrow(265,80,"up")
    arrow(330,80,"down")
    arrow(445,80,"right")
    
#--------------------------------------Draw the opening screen------------------------------------------------------------------------------------------
def openingScreen():                #the "welcome" screen
    while True:
        Draw.setBackground(Draw.BLACK)
        Draw.setColor(Draw.BLUE)
        Draw.setFontFamily("Rockwell")
        Draw.setFontSize(50)
        Draw.setFontBold(True)
        Draw.string("TAP-TAP REVOLUTION", 25, 200)
        Draw.setFontSize(30)
        Draw.setColor(Draw.WHITE)
        Draw.string("-Press any key-",180,300)
        if Draw.hasNextKeyTyped():
            flushKeys()
            instructions()       
                
def instructions():             #the screen with the instructions
    while True:
        Draw.clear()
        Draw.setBackground(Draw.BLACK)
        Draw.setColor(Draw.WHITE)
        Draw.setFontFamily("Arial Rounded MT Bold")
        Draw.setFontSize(25)
        Draw.string("How to play:\n Press the corresponding arrow key when the rising \narrow passes over the arrow on top.",30,20)  
        Draw.string("For every arrow correctly pressed,\n the score increases by 5.\n For every arrow missed, the score decreases by 5\n and 1 life is lost.\n The game is over when all lives are lost.", 30, 175)
        Draw.setColor(Draw.BLUE)
        Draw.string("-Press Enter to start-", 150, 400)
        Draw.show()
        if Draw.hasNextKeyTyped():
            playGame()    
#----------------------------Clear all previously pressed keys--------------------------------------------------------------------------------------------
        
def flushKeys():
    while Draw.hasNextKeyTyped():
        newKey = Draw.nextKeyTyped()
                    
#----------------------------------------Draw the score so that it is displayed on the screen------------------------------------------------------------
def drawScore(score):
    Draw.setColor(Draw.BLACK)
    score = str(score)
    Draw.setFontSize(33)
    Draw.string(score,608,40)
#----------------------------------------Draw lives so that they are displayed on the screen-------------------------------------------------------------
def drawLives(lives):
    Draw.setColor(Draw.BLACK)
    lives = str(lives)
    Draw.setFontSize(35)
    Draw.string(lives,610,110)               
#----------------------------------make the list of arrows that will be "rising" up the screen as the window passes over them--------------------------------------------
def makeArrowList():  
    arrowList = []
    direction = ["up","down","left","right"]
    numbers = [250, 200, 300, 380, 180]         #the possible distance between each row of arrows in the list along the y axis
    amountArrowsList = [1,2]                    # the number of arrows per row
    newY = 600          
    amountArrows = random.choice(amountArrowsList)
    for i in range(0,6000):                     #the arrowlist will have 6000 rows
        amountArrows = random.choice(amountArrowsList)
        newY = newY + random.choice(numbers)
        for j in range(amountArrows):  
            singleOrientation = random.choice(direction)
            if singleOrientation == "right":
                x = 445 
                
            elif singleOrientation == "left":
                x = 140
            elif singleOrientation == "up":
                x = 265
            elif singleOrientation == "down":
                x = 330
            newlist = [x , newY, singleOrientation]        #add the x, y, and orientation parameter for the arrowlist
            arrowList.append(newlist)
    return arrowList
#--------------------------------------------Actually draw the arrows in the arrowList-------------------------------------------------------------------------
def drawArrowList(arrowList, windowY):
    for each in arrowList:
        if each[1]-windowY > 0 and each[1]- windowY < canvasHeight:     #draws the arrows that fall within the windowY 
            arrow(each[0], each[1]-windowY, each[2])
            newlist = [each[0], each[1] -windowY, each[2]]
            
            
    return windowY

    
#-----------------------------Create a function to know if an arrow from the arrowList is overlapping with the arrows on the top of the screen--------------------------------    
    
def overlapArrows(arrowList, windowY):
    dict = {"Right":0, "Left":0, "Up":0, "Down":0}
    overlappedArrow = "none"
    for each in arrowList:
                #gives extra room for the arrows to be considered overlapping 
        if each[2] == "left":  
            if each[1] - windowY < 105 and each[1] - windowY > 60 or\
                each[1] - windowY <80   and each[1] - windowY > 60:
                overlappedArrow = "Left"
                dict["Left"] += 1
           
        if each[2] == "right":
            if each[1] - windowY < 105 and each[1] - windowY > 60 or\
               each[1] - windowY <80   and each[1] - windowY >60:
                overlappedArrow = "Right"
                dict["Right"] += 1
        if each[2] == "up":
            if each[1] - windowY < 105 and each[1] - windowY > 80 or\
               each[1] - windowY <80   and each[1] - windowY  >60:
                overlappedArrow = "Up"
                dict["Up"] += 1
        if each[2] == "down":
            if each[1] - windowY < 110 and each[1] - windowY > 80 or\
               each[1] - windowY <80   and each[1] - windowY >60:
                overlappedArrow = "Down"
                dict["Down"] += 1
    
    return overlappedArrow, dict   

#---------------------------------------Define the increment that the speed will be increasing by--------------------------------------------------------    
def windowSpeed(score,speed, changed):
    if score == 0:
        speed = 2
    elif score <= 250 and score % 35 == 0 and changed == False:
        speed += 0.7
        changed = True
    return speed, changed

#------------------------------if lost all lives, end game------------------------------------------------------------------------------------------------
def endGame(lives, score):
    while lives == 0:
        Draw.clear()
        Draw.setBackground(Draw.BLACK)
        Draw.setColor(Draw.RED)
        Draw.setFontSize(35)
        Draw.setFontFamily("Rockwell")
        Draw.string("GAME OVER", 200, 250)
        score = str(score)
        Draw.setColor(Draw.WHITE)   
        Draw.string("Final Score:", 200, 300)
        Draw.string(score, 440, 300)
        Draw.show()
#--------------------------------------------Draw the board with the everything--------------------------------------------------------------------------------
def drawBoard(windowY, score, lives, arrowList,key):
    Draw.clear()
    setBoard()
    windowY = drawArrowList(arrowList, windowY)
    Draw.setFontFamily("Lucida Grande")
    score = drawScore(score)
    lives = drawLives(lives)
    Draw.show()        
#------------------------------To play the game----------------------------------------------------------------------------------------------------------
def playGame():
    speed = 2
    arrowList = makeArrowList()
    changed = False
    score = 0
    oldScore = 0
    lives = 4
    windowY = 0
    key = ""
    drawBoard(windowY, score, lives, arrowList,key)  #draw the board to be displayed
    while lives > 0:
        
        if Draw.hasNextKeyTyped():                  # if user typed an arrow key
            key = Draw.nextKeyTyped()   
            if key == "Left" or key == "Right" or key == "Up" or key == "Down":
                overlappedArrow, dict = overlapArrows(arrowList, windowY)
                if dict[key] == 1:
                    score += 5
                else:
                    score -= 5
                    lives -= 1         

        if (oldScore != score):         #increment windowY by the speed
            changed = False
            oldScore = score
        speed, changed = windowSpeed(score,speed, changed)
        windowY += speed
        drawBoard(windowY, score, lives, arrowList,key)
        
    endGame(lives, score)           #if lives == 0 end game
               
#-----------------------------------------Create a main function that will run the whole game-----------------------------------------------------
def main():
    openingScreen()
   
#-----------------------------------------Invoke the game--------------------------------------------------------------------------------------------------    
main()


