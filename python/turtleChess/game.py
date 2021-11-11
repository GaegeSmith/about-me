from globals import *
from SquareTurtle import *
from useful import *
from pieces import *

Terminal.clear()

# scaling feature where it uses percent
# wn = Screen()
scaleFactor = 0.75
# wnWidth = 1600 * scaleFactor  # kinda what I did here
# wnHeight = 900  * scaleFactor
squareSize = 100 * scaleFactor
# wn.setup(wnWidth, wnHeight)
# wn.mode('world')
# wn.setworldcoordinates(-wnWidth / 2, -wnHeight / 2, wnWidth / 2, wnHeight / 2)
# wn.bgcolor('#465C5B')

takenByWhite = []
takenByBlack = []

boardTurts = []
currColor = 'white'
loser = ''




'''
#FFFFFF
#68F466

# E5E100
# 1A1DC5
'''




def newBoardTurt(shapeSize):
    drawBoi = Turtle()
    # drawBoi.color('#C04000')
    # drawBoi.shape('square')
    drawBoi.penup()
    drawBoi.speed(0)
    drawBoi.goto(50000, 0)
    drawBoi.shapesize(shapeSize)
    drawBoi = SquareTurt(drawBoi)
    return drawBoi


# reused function, slight modification
# this function makes a checkerboard pattern of turtles, with the center at (x, y)
def checkerBoard(x0, y0):
    global boardTurts, squareSize
    xval = (x0 - squareSize * 4) - squareSize / 2
    yval = (y0 + squareSize * 4) - squareSize / 2
    
    xLimit = xval + squareSize * 8
    yLimit = yval - squareSize * 7

    shapeSize = squareSize / 20


    drawBoi = newBoardTurt(shapeSize)
    # color = '#C04000'
    color = 'light'
    x = xval
    i = 0
    while (x < xLimit):
        boardTurts.append(list())
        x = x + squareSize
        y = yval
        
        
        drawBoi = newBoardTurt(shapeSize)
        drawBoi.turt.goto(x,y)
        # drawBoi.turt.color(color)
        drawBoi.turt.shape((BOARDIMGS[color]))


        boardTurts[i].append(drawBoi)

        # print('hello there')
        while (y > yLimit):
            # print('general kenobi')
            drawBoi = newBoardTurt(shapeSize)
            y = y - squareSize
            drawBoi.turt.goto(x,y)

            
            if color == 'dark':
                color = 'light'
            elif color == 'light':
                color = 'dark'

            drawBoi.turt.shape((BOARDIMGS[color]))

            # if color == '#C04000':
            #     color = '#FFFDD0'
            # elif color == '#FFFDD0':
            #     color = '#C04000'
                
            # drawBoi.turt.color(color)


            boardTurts[i].append(drawBoi)
        i += 1

    # drawBoi.turt.hideturtle()
    boardTurts = Grid.rot90(boardTurts)


def genBoard():
    checkerBoard(0, 0)

    # assign the onclick function boardTurtles 
    for row in range(len(boardTurts)):

        for col in range(len(boardTurts[row])):
            boardTurts[row][col].turt.onclick(boardTurts[row][col].clicked)
            boardTurts[row][col].RC = (row, col)

    # adds black pawns to the board
    for i in range(len(globals.board[1])):
        tmpTurt = Turtle()
        tmpTurt.speed(10)
        globals.board[1][i] = Pawn(tmpTurt, "black", (1, i))

    # adds white pawns to the board
    for i in range(len(globals.board[6])):
        tmpTurt = Turtle()
        tmpTurt.speed(10)
        globals.board[6][i] = Pawn(tmpTurt, "white", (6, i))

    # for each color and that color's row
    for color in [('white', 7), ('black', 0)]:
        i = 0
        # add the piece that goes there, the pieces behind the pawns
        for piece in [f'Rook(tmpTurt, "{color[0]}", ({color[1]}, i))', f'Knight(tmpTurt, "{color[0]}", ({color[1]}, i))', f'Bishop(tmpTurt, "{color[0]}", ({color[1]}, i))', f'Queen(tmpTurt, "{color[0]}", ({color[1]}, i))', f'King(tmpTurt, "{color[0]}", ({color[1]}, i))', f'Bishop(tmpTurt, "{color[0]}", ({color[1]}, i))', f'Knight(tmpTurt, "{color[0]}", ({color[1]}, i))', f'Rook(tmpTurt, "{color[0]}", ({color[1]}, i))']:
            tmpTurt = Turtle()
            tmpTurt.speed(10)
            globals.board[color[1]][i] = eval(piece)
            i += 1
    
    # move all the pieces where they go, and assign the click function
    for row in range(len(boardTurts)):
        for col in range(len(boardTurts[row])):

            try:
                globals.board[row][col].turt.onclick(globals.board[row][col].clicked)
                globals.board[row][col].turt.goto(boardTurts[row][col].turt.pos())
                if globals.board[row][col].turt.pos() == boardTurts[row][col].turt.pos():
                    boardTurts[row][col].turt.hideturtle()

            except:
                "you didn't succeed"


def resetSelection():

    if ("Pawn" in str(type(globals.selPiece))):
        globals.selPiece.turt.shape(PIECESIMGS[f'{globals.selPiece.color[0]}pawn'])

    elif ("Bishop" in str(type(globals.selPiece))):
        globals.selPiece.turt.shape(PIECESIMGS[f'{globals.selPiece.color[0]}bishop'])

    elif ("Rook" in str(type(globals.selPiece))):
        globals.selPiece.turt.shape(PIECESIMGS[f'{globals.selPiece.color[0]}rook'])

    elif ("Knight" in str(type(globals.selPiece))):
        globals.selPiece.turt.shape(PIECESIMGS[f'{globals.selPiece.color[0]}knight'])

    elif ("Queen" in str(type(globals.selPiece))):
        globals.selPiece.turt.shape(PIECESIMGS[f'{globals.selPiece.color[0]}queen'])

    elif ("King" in str(type(globals.selPiece))):
        globals.selPiece.turt.shape(PIECESIMGS[f'{globals.selPiece.color[0]}king'])

    globals.selPiecePos = (0, 0)
    globals.selSquarePos = (0, 0)
    globals.selSquare = ''
    globals.selPiece = ''
    globals.pieceRC = (0, 0)
    globals.squareRC = (0, 0)

def pieceCantMove(piece):
    piece.wiggleWiggleWiggle()
    resetSelection()

def checkGameOver():
    global loser
    for color in ['black', 'white']:
        # print(color)
        for row in globals.board:
            for space in row:
                # print(type(space))
                if type(space) == King and space.color == color:
                    # print('found')
                    gameOver = False
                    loser = ''
                    break

                else:
                    gameOver = True
                    # print('not found', color)
                    loser = color
                    
            if not gameOver:
                break
        

        if gameOver:
            # print('bye')
            time.sleep(0.5)
            quit()

def clicked(x, y):
    global currColor
    
    # print(globals.pieceRC, 'pieces')
    # print(globals.squareRC, 'square')

    # movement, if a piece to move and a space to move to / piece to take have been selected
    # check if it is valid move, if not wiggle wiggle wiggle
    # if so, move the piece and change visibility of board squares accordingly, then switch turns and reset selection
    if globals.selPiecePos != (0, 0) and globals.selSquarePos != (0, 0):
        if globals.board[globals.pieceRC[0]][globals.pieceRC[1]].color == currColor:
            if globals.board[globals.pieceRC[0]][globals.pieceRC[1]].canMove(globals.pieceRC, globals.squareRC, globals.board):
                
                # print(f"hello{boardTurts[3][3]}{board[3][3]}there")
                # print(globals.selPiece.color)
                defendingPiece = board[globals.squareRC[0]][globals.squareRC[1]]
                if (type(defendingPiece) != str) and defendingPiece.color != globals.selPiece.color:
                    if (defendingPiece.color == "black"):
                        defendingPiece.calcTakenPos()
                        takenByWhite.append(defendingPiece)

                    if (defendingPiece.color == "white"):
                        defendingPiece.calcTakenPos()
                        takenByBlack.append(defendingPiece)

                
                # print(globals.pieceRC)
                # piece movement
                globals.board[globals.pieceRC[0]][globals.pieceRC[1]].move(globals.pieceRC, globals.squareRC, globals.board)

                

                globals.selSquare.turt.hideturtle()
                globals.selPiece.turt.goto(globals.selSquarePos)
                boardTurts[globals.pieceRC[0]][globals.pieceRC[1]].turt.showturtle()
                
                if type(globals.selPiece) == Pawn:
                    globals.selPiece.promote(board, globals.selSquare.RC)

                if currColor == 'white':
                    currColor = 'black'
                elif currColor == 'black':
                    currColor = 'white'
            elif type(globals.selPiece) == King:
                castling = globals.board[globals.pieceRC[0]][globals.pieceRC[1]].castle(globals.pieceRC, globals.squareRC, globals.board)
                # print(castling)
                
                if castling[0]:
                    
                    boardTurts[
                        globals.selSquare.RC[0]
                        ][
                        globals.selSquare.RC[1] - castling[2]
                    ].turt.hideturtle()
                    
                    boardTurts[castling[1].RC[0]][castling[1].RC[1]].turt.showturtle()



                    castling[1].turt.goto(
                            boardTurts[
                            globals.selSquare.RC[0]
                            ][
                            globals.selSquare.RC[1] - castling[2]
                            ].turt.pos()
                        )


                    castling[1].castle(globals.selPiece, board, castling[2])
                    globals.selSquare.turt.hideturtle()
                    globals.selPiece.turt.goto(globals.selSquarePos)
                    boardTurts[globals.pieceRC[0]][globals.pieceRC[1]].turt.showturtle()

                    if currColor == 'white':
                        currColor = 'black'
                    elif currColor == 'black':
                        currColor = 'white'
                else:
                    pieceCantMove(globals.board[globals.pieceRC[0]][globals.pieceRC[1]])

            else:
                pieceCantMove(globals.board[globals.pieceRC[0]][globals.pieceRC[1]])
                
        else:
            pieceCantMove(globals.board[globals.pieceRC[0]][globals.pieceRC[1]])
            
        # print(Grid.build(globals.board))
        resetSelection()

    checkGameOver()
