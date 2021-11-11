from useful import *
from game import *


"""
GUI
    buttons
    resizing the buttons
    transparent buttons
    different windows
        pvc
        pvp
        directions
            how to play chess
        credits
            all the looking up stuff, and Mr Bander
        
        back button

Game
    drawing board, each square is turtle
    pieces as turtles
    lots of lists
    movements, which were technically already done
"""

onHome = True

#create a window
wn = Screen()
bgpic(f'{Terminal.filePath()}{dataFile}/background.gif')
image = f"{Terminal.filePath()}{dataFile}/source.gif"



scaleFactor = 0.75
wnWidth = 1600 * scaleFactor
wnHeight = 900  * scaleFactor
wn.setup(wnWidth, wnHeight)
wn.mode('world')
wn.setworldcoordinates(-wnWidth / 2, -wnHeight / 2, wnWidth / 2, wnHeight / 2)

for img in BOARDIMGS:
    wn.addshape(BOARDIMGS[img])

for img in PIECESIMGS:
    wn.addshape(PIECESIMGS[img])

for img in BTNIMGS:
    wn.addshape(BTNIMGS[img])


addshape(image)
#define user cursor and font sizes
cursor_size = 15
font_size = 50
direct_size = 20
credit_font_size = 20
fontSettings = ('Arial', font_size, 'bold')
directionFontSettings = ('Arial', direct_size, 'bold')
creditFontSettings = ('Arial', credit_font_size, 'bold')
#welcome text

# def motion(event):
#     x, y = event.x, event.y
#     print(f'{x}, {y}')

# wn.getcanvas().bind('<Motion>', motion)


#loading functions for screens in the menu
def hideTurtleButtons():
    global creditButton, directionsButton, pvpButton, pvcButton
    creditButton.clear()
    directionsButton.clear()
    pvpButton.clear()
    pvcButton.clear()

    pvcButton.hideturtle()
    pvpButton.hideturtle()
    creditButton.hideturtle()
    directionsButton.hideturtle()
    pvcButton.clear()
    pvpButton.clear()
    directionsButton.clear()
    creditButton.clear()

def showTurtleMenu(x, y):
    global onHome
    if onHome:
        quit()
    creditButton.clear()
    directionsButton.clear()
    pvpButton.clear()
    pvcButton.clear()
    genBtns()
    assignClicks()
    onHome = True

def pvc(x, y):
    global onHome
    onHome = False
    print("board will summon here")
    hideTurtleButtons()


def pvp(x, y):
    global onHome
    onHome = False
    # print("board will summon here")
    hideTurtleButtons()
    backButton.clear()
    backButton.hideturtle()
    
    bgpic(BOARDIMGS['boardBg'])
    genBoard()
    wn.onclick(clicked)


def directions(x, y):
    global onHome
    onHome = False
    hideTurtleButtons()
    directionsButton.sety(directionsButton.ycor() - 175)
    directionsButton.write("Welcome to chess, the following will teach you how to play\n\nWhite always moves first \n\nThe pawn can move one space in front of it, and can only take an \nenemy piece if it is diagonal from the pawn by moving in the space \nwhere the enemy piece was. \n\nRook can move as many spaces directly vertical \nor horizontal as you desire until it reaches \nanother piece, or the edge of the board \n\nKnight can move in one direction vertically or horizintally \n3 spaces, then whichever direction not chosen one space, regardless of \npieces in the way of movement, as long as your own piece \nis not where the knight will land. \n\nBishops can move in any direction diagonal, but never \nleave the color space it is on, and can move into \nan enemy piece, up to the square before it's own space, \nand up until the board edge \n\nQueen has the powers and limitations of the rook and bishop combined \n\nKing can move in any direction one space, as long as not one of his own pieces \nare blocking the space, he won't fall off the board, \nand is not in danger of being taken by another piece", align='center', font=direct_size)

def credits(x, y):
    global onHome
    onHome = False
    hideTurtleButtons()
    creditButton.write("https://stackoverflow.com/questions/59902849/how-can-i-create-a-button-in-turtle \n\nhttps://docs.python.org/3/library/turtle.html \n\nMr. Bander\n\n\nHad a lot of emotional support from Eric", align='center', font=creditFontSettings)


def assignClicks():
    pvcButton.onclick(pvc)
    pvpButton.onclick(pvp)
    directionsButton.onclick(directions)
    creditButton.onclick(credits)
    backButton.onclick(showTurtleMenu)

def genBtns():
    global creditButton, directionsButton, pvpButton, pvcButton
    #pvc turtle menu option
    pvcButton=Turtle()
    pvcButton.hideturtle()
    pvcButton.fillcolor("#FFFFFF")
    pvcButton.color("#FFFFFF")
    pvcButton.shape(BTNIMGS['pvc'])
    pvcButton.penup()
    pvcButton.goto(0,210)
    # pvcButton.write("PvC Chess", align='center', font=fontSettings)
    pvcButton.sety(185 + cursor_size + font_size)
    pvcButton.showturtle()

    #pvp turtle menu option
    pvpButton=Turtle()
    pvpButton.hideturtle()
    pvpButton.fillcolor("#FFFFFF")
    pvpButton.color("#FFFFFF")
    pvpButton.shape(BTNIMGS['pvp'])
    pvpButton.penup()
    pvpButton.goto(0,80)
    # pvpButton.write("PvP Chess", align='center', font=fontSettings)
    pvpButton.sety(50 + cursor_size + font_size)
    pvpButton.showturtle()

    #directions turtle menu option
    directionsButton=Turtle()
    directionsButton.hideturtle()
    directionsButton.pencolor("#FFFFFF")
    directionsButton.color("#FFFFFF")
    directionsButton.shape(BTNIMGS['dir'])
    directionsButton.penup()
    directionsButton.goto(0,-50)
    # directionsButton.write("Directions", align='center', font=fontSettings)
    directionsButton.sety(-80 + cursor_size + font_size)
    directionsButton.showturtle()

    #credits turtle menu option
    creditButton=Turtle()
    creditButton.hideturtle()
    creditButton.pencolor("#FFFFFF")
    creditButton.color("#FFFFFF")
    creditButton.shape(BTNIMGS['creds'])
    creditButton.penup()
    creditButton.goto(0,-180)
    # creditButton.write("Credits", align='center', font=fontSettings)
    creditButton.sety(-210 + cursor_size + font_size)
    creditButton.showturtle()


backButton=Turtle()
backButton.hideturtle()
backButton.shape('square')
backButton.pencolor("#FFFFFF")
backButton.penup()
backButton.goto(0,-300)
backButton.fillcolor('white')
backButton.write("Back", align='center', font=fontSettings)
backButton.sety(-290 + cursor_size + font_size)
backButton.showturtle()

genBtns()
assignClicks()
for turt in turtles():
    turt.speed(0)
wn.mainloop()