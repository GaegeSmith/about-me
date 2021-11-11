from useful import *
from turtle import *
selPiecePos = (0, 0)
selSquarePos = (0, 0)
selSquare = ''
selPiece = ''
pieceRC = (0, 0)
squareRC = (0, 0)
board = Grid.create(8, 8)
bPawnsCap = 0
wPawnsCap = 0
bPiecesCap = 0
wPiecesCap = 0
dataFile = "data"
firstMoveMade = False

BOARDIMGS = {
    'dark' : f'{Terminal.filePath()}{dataFile}/boardDark.gif',
    'light' : f'{Terminal.filePath()}{dataFile}/boardLight.gif',
    'boardBg' : f'{Terminal.filePath()}{dataFile}/boardBg.gif',
}

BTNIMGS = {
    'pvc' : f'{Terminal.filePath()}{dataFile}/pvcBtn.gif',
    'pvp' : f'{Terminal.filePath()}{dataFile}/pvpBtn.gif',
    'dir' : f'{Terminal.filePath()}{dataFile}/dirBtn.gif',
    'creds' : f'{Terminal.filePath()}{dataFile}/credBtn.gif',
}
