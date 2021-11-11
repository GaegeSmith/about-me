from useful import *
import globals
from SquareTurtle import SquareTurt



PIECESIMGS = {
    'bbishop' : f'{Terminal.filePath()}{globals.dataFile}/BBishop.gif',
    'bking' : f'{Terminal.filePath()}{globals.dataFile}/BKing.gif',
    'bknight' : f'{Terminal.filePath()}{globals.dataFile}/BKnight.gif',
    'bpawn' : f'{Terminal.filePath()}{globals.dataFile}/BPawn.gif',
    'bqueen' : f'{Terminal.filePath()}{globals.dataFile}/BQueen.gif',
    'brook' : f'{Terminal.filePath()}{globals.dataFile}/BRook.gif',
    'wbishop' : f'{Terminal.filePath()}{globals.dataFile}/WBishop.gif',
    'wking' : f'{Terminal.filePath()}{globals.dataFile}/WKing.gif',
    'wknight' : f'{Terminal.filePath()}{globals.dataFile}/WKnight.gif',
    'wpawn' : f'{Terminal.filePath()}{globals.dataFile}/WPawn.gif',
    'wqueen' : f'{Terminal.filePath()}{globals.dataFile}/WQueen.gif',
    'wrook' : f'{Terminal.filePath()}{globals.dataFile}/WRook.gif',

    'bbishopsel' : f'{Terminal.filePath()}{globals.dataFile}/BBishopSel.gif',
    'bkingsel' : f'{Terminal.filePath()}{globals.dataFile}/BKingSel.gif',
    'bknightsel' : f'{Terminal.filePath()}{globals.dataFile}/BKnightSel.gif',
    'bpawnsel' : f'{Terminal.filePath()}{globals.dataFile}/BPawnSel.gif',
    'bqueensel' : f'{Terminal.filePath()}{globals.dataFile}/BQueenSel.gif',
    'brooksel' : f'{Terminal.filePath()}{globals.dataFile}/BRookSel.gif',
    'wbishopsel' : f'{Terminal.filePath()}{globals.dataFile}/WBishopSel.gif',
    'wkingsel' : f'{Terminal.filePath()}{globals.dataFile}/WKingSel.gif',
    'wknightsel' : f'{Terminal.filePath()}{globals.dataFile}/WKnightSel.gif',
    'wpawnsel' : f'{Terminal.filePath()}{globals.dataFile}/WPawnSel.gif',
    'wqueensel' : f'{Terminal.filePath()}{globals.dataFile}/WQueenSel.gif',
    'wrooksel' : f'{Terminal.filePath()}{globals.dataFile}/WRookSel.gif',
}

SHAKELIST = [
    (1, 0),
    (-3, -1),
    (4, -1),
    (2, 4),
    (-12, -5),
    (6, 3)
]
class Piece:
    def creation(self, turt, color, RC):
        self.turt = turt
        self.color = color
        self.turt.penup()
        self.RC = RC
        self.taken = False
        self.hasMoved = False

    def wiggleWiggleWiggle(self):
        coords = self.turt.pos()

        for vel in SHAKELIST:
            newPos = self.turt.pos()
            newPos = (newPos[0] + vel[0], newPos[1] + vel[1])

            self.turt.goto(newPos)


        self.turt.seth(0)
        self.turt.goto(coords)

    def moveCap(self, coords):
        self.wiggleWiggleWiggle()
        time.sleep(0.01)
        self.turt.goto(coords[0], coords[1])
        self.turt.showturtle()
        self.turt.stamp()

    def calcTakenPos(self):
        
        Terminal.clear()
        
        if self.color == "white" and type(self) == Pawn:
            self.moveCap((-550, 300 - (globals.wPawnsCap * 70)))
            globals.wPawnsCap += 1

        elif self.color == "white":
            self.moveCap((-470, 300 - (globals.wPiecesCap * 70)))
            globals.wPiecesCap += 1

        elif self.color == "black" and type(self) == Pawn:
            self.moveCap((550, 300 - (globals.bPawnsCap * 70)))
            globals.bPawnsCap += 1
        
        elif self.color == "black":
            self.moveCap((470, 300 - (globals.bPiecesCap * 70)))
            globals.bPiecesCap += 1

    def clicked(self, x, y):
        self.RC = Grid.find(globals.board, self)
        
        # try:
        #     print(type(globals.selSquare) != SquareTurt, type(globals.selPiece) != str, globals.selPiece.color != self.color)
        # except:
        #     print(type(globals.selSquare) != SquareTurt, type(globals.selPiece) != str, 'no color')
        
        if type(globals.selSquare) != SquareTurt and type(globals.selPiece) != str and globals.selPiece.color != self.color:
            globals.selSquare = self
            globals.selSquarePos = self.turt.pos()
            globals.squareRC = self.RC
        else:
            self.selected()
            globals.selPiecePos = self.turt.pos()
            globals.selPiece = self
            globals.pieceRC = self.RC

    def isPathBlocked(self, fromHere, toHere, board):
        # setup end point of desired path
        endPos = Grid.Point(toHere[0], toHere[1])

        # find the change in x
        stepX = toHere[0] - fromHere[0]
        # if change in x is positive, set it to 1, if negative set to -1
        if stepX < 0:
            stepX = -1
        elif stepX > 0:
            stepX = 1
        
        # find the change in y
        stepY = toHere[1] - fromHere[1]
        # if change in y is positive, set it to 1, if negative set to -1
        if stepY < 0:
            stepY = -1
        elif stepY > 0:
            stepY = 1

        # setup the pos to be checked
        tempPos = Grid.Point(fromHere[0], fromHere[1])
        
        tempPos.x += stepX
        tempPos.y += stepY

        # check each position on the path the selected piece would take to get to the desired space
        #   if said space is not clear, '   ', return true
        while (tempPos.x != endPos.x or tempPos.y != endPos.y):
            
            if board[tempPos.x][tempPos.y] != ' ':
                # print('path is blocked', board[tempPos.x][tempPos.y])
                return True
            tempPos.x += stepX
            tempPos.y += stepY
        
        # else return False

        return False

    def selected(self):
        
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


        if ("Pawn" in str(type(self))):
            self.turt.shape(PIECESIMGS[f'{self.color[0]}pawnsel'])

        elif ("Bishop" in str(type(self))):
            self.turt.shape(PIECESIMGS[f'{self.color[0]}bishopsel'])

        elif ("Rook" in str(type(self))):
            self.turt.shape(PIECESIMGS[f'{self.color[0]}rooksel'])

        elif ("Knight" in str(type(self))):
            self.turt.shape(PIECESIMGS[f'{self.color[0]}knightsel'])

        elif ("Queen" in str(type(self))):
            self.turt.shape(PIECESIMGS[f'{self.color[0]}queensel'])

        elif ("King" in str(type(self))):
            self.turt.shape(PIECESIMGS[f'{self.color[0]}kingsel'])

    def isEmpty(self, toHere, board):
        if board[toHere[0]][toHere[1]] == ' ':
            # print('space is empty')
            return True
        return False

    def isAttackingOwnTeam(self, ownColor, defendingPiece):
        # print(ownColor, 'hello', str(defendingPiece))
        try:
            if ownColor == defendingPiece.color:
                # print('attacking own team')
                return True
            return False
        except:
            return False

    # moves whatever is at ideces fromHere to ideces toHere, and sets fromHere to "   "
    def move(self, fromHere, toHere, board):
        globals.firstMoveMade = True
        board[toHere[0]][toHere[1]] = board[fromHere[0]][fromHere[1]]
        board[fromHere[0]][fromHere[1]] = ' '
        self.RC = toHere
        self.hasMoved = True



# king is an extension of Piece, meaning all the stuff inside Piece is inside king, and all the other pieces too
class King(Piece):
    def __init__(self, turtle, color, RC):
        self.creation(turtle, color, RC)
        self.turt.shape(PIECESIMGS[color[0] + 'king'])
        self.chr = 'K'

    def castle(self, fromHere, toHere, board):
        result = (False, False, False)
        if toHere[0] == fromHere[0]:
            if self.color == "black":
                row = 0
            else:
                row = 7

            if toHere[1] > fromHere[1] and abs(toHere[1] - fromHere[1]) == 2:
                direction = 1
                rook = board[row][7]
                # rook.castle(self, board, direction)
                result = (True, rook, direction)

            elif toHere[1] < fromHere[1] and abs(toHere[1] - fromHere[1]) == 2:
                direction = -1
                rook = board[row][0]
                # rook.castle(self, board, direction)
                result = (True, rook, direction)
        
        return result

    def canMove(self, fromHere, toHere, board):
        if abs(toHere[0] - fromHere[0]) == 2 and toHere[1] == fromHere[1]:
            self.castle(toHere, fromHere, board)
            return False

        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False
        
        if abs(toHere[0] - fromHere[0]) <= 1 and abs(toHere[1] - fromHere[1]) <= 1:
            return True
        
        return False

    def __str__(self):
        return f'{self.chr}'

class Queen(Piece):
    def __init__(self, turtle, color, RC):
        self.creation(turtle, color, RC)
        self.turt.shape(PIECESIMGS[color[0] + 'queen'])
        self.chr = 'Q'

    def canMove(self, fromHere, toHere, board):
        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False
        
        if self.isPathBlocked(fromHere, toHere, board):
            return False

        # if the desired move is horizontal or diagonal
        if (
            fromHere[0] == toHere[0] or fromHere[1] == toHere[1]
            or
            abs(toHere[0] - fromHere[0]) == abs(toHere[1] - fromHere[1])
        ):
            return True

        return False

    def __str__(self):
        return f'{self.chr}'

class Bishop(Piece):
    def __init__(self, turtle, color, RC):
        self.creation(turtle, color, RC)
        self.turt.shape(PIECESIMGS[color[0] + 'bishop'])
        self.chr = 'B'

    def canMove(self, fromHere, toHere, board):
        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False

        if self.isPathBlocked(fromHere, toHere, board):
            return False

        # checks if the desired move is a diagonal move
        if abs(toHere[0] - fromHere[0]) == abs(toHere[1] - fromHere[1]):
            return True

        return False

    def __str__(self):
        return f'{self.chr}'

class Knight(Piece):
    def __init__(self, turtle, color, RC):
        self.creation(turtle, color, RC)
        self.turt.shape(PIECESIMGS[color[0] + 'knight'])
        self.chr = 'H'

    def canMove(self, fromHere, toHere, board):
        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False

        # checking for the L shape, deltaX = 2 and deltaY = 1, or deltaX = 1 and deltaY = 2
        if (
            (abs(toHere[0] - fromHere[0]) == 2 and abs(toHere[1] - fromHere[1]) == 1)
            or
            (abs(toHere[0] - fromHere[0]) == 1 and abs(toHere[1] - fromHere[1]) == 2)
        ):
            return True

        return False

    def __str__(self):
        return f'{self.chr}'

class Rook(Piece):
    def __init__(self, turtle, color, RC):
        self.creation(turtle, color, RC)
        self.turt.shape(PIECESIMGS[color[0] + 'rook'])
        self.chr = 'R'

    def canMove(self, fromHere, toHere, board):
        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False

        if self.isPathBlocked(fromHere, toHere, board):
            return False


        # check if move is straight line
        if fromHere[0] == toHere[0] or fromHere[1] == toHere[1]:
            return True
        
        return False

    def castle(self, king:King, board, direction):
        if self.hasMoved or king.hasMoved or self.isPathBlocked(self.RC, king.RC, board):
            self.wiggleWiggleWiggle()
            king.wiggleWiggleWiggle()
            globals.selSquare = ''
            globals.squareRC = (0, 0)
            globals.selSquarePos = (0, 0)

        else:
            if direction == -1:
                # left
                king.move(king.RC, (king.RC[0], king.RC[1] - 2), board)
                self.move(self.RC, (self.RC[0], self.RC[1] + 3), board)

            elif direction == 1:
                # right
                king.move(king.RC, (king.RC[0], king.RC[1] + 2), board)
                self.move(self.RC, (self.RC[0], self.RC[1] - 2), board)

    def __str__(self):
        return f'{self.chr}'

class Pawn(Piece):
    def __init__(self, turtle, color, RC):
        self.creation(turtle, color, RC)
        self.turt.shape(PIECESIMGS[color[0] + 'pawn'])
        self.chr = 'P'

        # checks if the pawn is attacing, if not check if there is a piece where it wants to go

    def validPawnMove(self, toHere, fromHere, board):
        # print(abs(toHere[0] - fromHere[0]), abs(toHere[1] - fromHere[1]))
        if abs(toHere[0] - fromHere[0]) == abs(toHere[1] - fromHere[1]) and (not self.isEmpty(toHere, board)):
                return True
        else:
            if self.isEmpty(toHere, board) and abs(toHere[1] - fromHere[1]) == 0:
                return True
            else:
                return False

    def canMove(self, fromHere, toHere, board):

        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False

        # check if the pawn is moving the correct direction on the board
        if self.color == 'black':
            if (toHere[0] - fromHere[0] == 1 or ((not self.hasMoved) and toHere[0] - fromHere[0] == 2)) and self.validPawnMove(toHere, fromHere, board):
                
                return True

        elif self.color == 'white':
            if (toHere[0] - fromHere[0] == -1 or ((not self.hasMoved) and toHere[0] - fromHere[0] == -2)) and self.validPawnMove(toHere, fromHere, board):
                
                return True
        

        # check if the pawn is moving the correct direction on the board
        # only need to check if the pawn is moving -1 on y because the board flips
        # if toHere[0] - fromHere[0] == -1 and self.validPawnMove(toHere, fromHere, board):
        #     return True




        # for this piece, this line "should" never execute, but better safe than sorry
        return False

    def promote(self, board, currPosPawn):
        if self.color == "white" and currPosPawn[0] == 0:
            turt = globals.Turtle(shape = PIECESIMGS["wqueen"])
            turt.penup()
            turt.speed(0)
            turt.goto(self.turt.pos())

            board[currPosPawn[0]][currPosPawn[1]] = Queen(turt, "white", currPosPawn)
            turt.onclick(
                board[currPosPawn[0]][currPosPawn[1]].clicked
            )
            self.turt.hideturtle()
        
        
        elif self.color == "black" and currPosPawn[0] == 7:
            turt = globals.Turtle(shape = PIECESIMGS["bqueen"])
            turt.penup()
            turt.speed(0)
            turt.goto(self.turt.pos())
            board[currPosPawn[0]][currPosPawn[1]] = Queen(turt, "black", currPosPawn)
            turt.onclick(
                board[currPosPawn[0]][currPosPawn[1]].clicked
            )
            self.turt.hideturtle()

    def __str__(self):
        return f'{self.chr}'
