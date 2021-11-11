from useful import *
import globals

class SquareTurt:
    def __init__(self, turt):
        self.turt = turt
        self.RC = tuple()
    
    def clicked(self, x, y):
        if globals.selPiecePos != (0, 0):
            globals.selSquarePos = self.turt.pos()
            globals.selSquare = self
            globals.squareRC = self.RC