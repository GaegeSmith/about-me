from useful import *

# assing each piece a character, broke it out here so it would be easy to edit
kingTxt = 'K'
queenTxt = 'Q'
bishopTxt = 'B'
knightTxt = 'H'
rookTxt = 'R'
pawnTxt = 'P'


kingChr = {
    'black' : f' {Terminal.Color.DARKGREY}{kingTxt}{Terminal.Color.END} ',
    'white' : f' {Terminal.Color.WHITE}{kingTxt}{Terminal.Color.END} ',
    }
queenChr = {
    'black' : f' {Terminal.Color.DARKGREY}{queenTxt}{Terminal.Color.END} ',
    'white' : f' {Terminal.Color.WHITE}{queenTxt}{Terminal.Color.END} ',
    }
bishopChr = {
    'black' : f' {Terminal.Color.DARKGREY}{bishopTxt}{Terminal.Color.END} ',
    'white' : f' {Terminal.Color.WHITE}{bishopTxt}{Terminal.Color.END} ',
    }
knightChr = {
    'black' : f' {Terminal.Color.DARKGREY}{knightTxt}{Terminal.Color.END} ',
    'white' : f' {Terminal.Color.WHITE}{knightTxt}{Terminal.Color.END} ',
    }
rookChr = {
    'black' : f' {Terminal.Color.DARKGREY}{rookTxt}{Terminal.Color.END} ',
    'white' : f' {Terminal.Color.WHITE}{rookTxt}{Terminal.Color.END} ',
    }
pawnChr = {
    'black' : f' {Terminal.Color.DARKGREY}{pawnTxt}{Terminal.Color.END} ',
    'white' : f' {Terminal.Color.WHITE}{pawnTxt}{Terminal.Color.END} ',
    }



class Piece:
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
            if board[tempPos.x][tempPos.y] != '   ':
                return True
            tempPos.x += stepX
            tempPos.y += stepY
        
        # else return False

        return False            
        

    def isEmpty(self, toHere, board):
        if board[toHere[0]][toHere[1]] == '   ':
            return True
        return False


    def isAttackingOwnTeam(self, ownColor, defendingPiece):
        # print(ownColor, 'hello', str(defendingPiece))
        try:
            if ownColor == defendingPiece.color:
                return True
            return False
        except:
            return False

    # moves whatever is at ideces fromHere to ideces toHere, and sets fromHere to "   "
    def move(self, fromHere, toHere, board):
        board[toHere[0]][toHere[1]] = board[fromHere[0]][fromHere[1]]
        board[fromHere[0]][fromHere[1]] = '   '

        

# king is an extension of Piece, meaning all the stuff inside Piece is inside king, and all the other pieces too
class King(Piece):
    def __init__(self, color):
        self.color = color
        self.chr = kingChr[color]
        self.stuff = super()

    def canMove(self, fromHere, toHere, board):
        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]].color):
            return False
        
        if abs(toHere[0] - fromHere[0]) <= 1 and abs(toHere[1] - fromHere[1]) <= 1:
            return True
        
        return False




    def __str__(self):
        return f'{self.chr}'

class Queen(Piece):
    def __init__(self, color):
        self.color = color
        self.chr = queenChr[color]


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
    def __init__(self, color):
        self.color = color
        self.chr = bishopChr[color]

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
    def __init__(self, color):
        self.color = color
        self.chr = knightChr[color]

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
    def __init__(self, color):
        self.color = color
        self.chr = rookChr[color]

    def canMove(self, fromHere, toHere, board):
        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False

        if self.isPathBlocked(fromHere, toHere, board):
            return False


        # check if move is horizontal
        if fromHere[0] == toHere[0] or fromHere[1] == toHere[1]:
            return True
        
        return False


    def __str__(self):
        return f'{self.chr}'

class Pawn(Piece):
    def __init__(self, color):
        self.color = color
        self.chr = pawnChr[color]
        
        # checks if the pawn is attacing, if not check if there is a piece where it wants to go
    def validPawnMove(self, toHere, fromHere, board):
        if abs(toHere[0] - fromHere[0]) == abs(toHere[1] - fromHere[1]) and not self.isEmpty(toHere, board):
                return True
        else:
            if self.isPathBlocked(fromHere, toHere, board):
                return False
            else:
                return True

    def canMove(self, fromHere, toHere, board):

        if self.isAttackingOwnTeam(self.color, board[toHere[0]][toHere[1]]):
            return False

        # check if the pawn is moving the correct direction on the board
        # if self.color == 'black':
            # if toHere[0] - fromHere[0] == 1 and self.validPawnMove(toHere, fromHere, board):
            #     return True

        # elif self.color == 'white':
            # if toHere[0] - fromHere[0] == -1 and self.validPawnMove(toHere, fromHere, board):
            #     return True
            
        # check if the pawn is moving the correct direction on the board
        # only need to check if the pawn is moving -1 on y because the board flips
        if toHere[0] - fromHere[0] == -1 and self.validPawnMove(toHere, fromHere, board):
                return True


            

        # for this piece, this line "should" never execute, but better safe that sorry
        return False


    def __str__(self):
        return f'{self.chr}'
