from pieces import *
from useful import *

Terminal.clear()
# creates the board, a 2d list
board = Grid.create(8, 8)


# mapping letters at the side of a chess board to list index
letters = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
}

# mapping numbers on the side of a chess board to list index
numbers = {
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
}



# adds black pawns to the board
for i in range(len(board[1])):
    board[1][i] = Pawn("black")

# adds white pawns to the baord
for i in range(len(board[6])):
    board[6][i] = Pawn("white")

# for each color and that color's row
for color in [('white', 7), ('black', 0)]:
    i = 0
    # add the piece that goes there, the pieces behind the pawns
    for piece in [f'Rook("{color[0]}")', f'Knight("{color[0]}")', f'Bishop("{color[0]}")', f'Queen("{color[0]}")', f'King("{color[0]}")', f'Bishop("{color[0]}")', f'Knight("{color[0]}")', f'Rook("{color[0]}")']:
        board[color[1]][i] = eval(piece)
        print(type(eval(piece)))
        i += 1



delay = 0.01

# current color's turn
currColor = Terminal.Color.WHITE

# fancy display board
Terminal.delayPrint(Grid.build(board), delay, False)



# the below stuff was used to write the move checkers in pieces.py, left it in to show first 

# def pawnMove(pawn):
#     for pieceColor in [Terminal.Color.DARKGREY, Terminal.Color.WHITE]:
#         if pawn in numbers + 1:
#             move()
#         elif color == color:
#                 print("Move invalid, own piece already in square.")
#         else:
#             print("Move was invalid")



# def rookMove(rook):
#     for pieceColor in [Terminal.Color.DARKGREY, Terminal.Color.WHITE]:
#         for i in range(board):
#             if rook in range(len(letters)) or range(len(numbers)):
#                 if rook != pieceColor or board == ' ':
#                     move()
#             elif pieceColor == color:
#                 print("Move was invalid, own piece already in square.")
#             elif rook in range(len(letters)) and range(len(numbers)):
#                 print("Move was invalid")
#                 #redo turn for user

            
# def knightMove(knight):
#     for pieceColor in [Terminal.Color.DARKGREY, Terminal.Color.WHITE]:
#         if knight in (letters +- 3 and numbers +- 2) or (letters +- 2 and numbers +- 3):
#             move()
#         elif pieceColor == color:
#             print("Move was invalid, own piece already in square")
#         else:
#             print("move was invalid")

# def bishopMove(bishop):
#     for pieceColor in [Terminal.Color.DARKGREY, Terminal.Color.WHITE]:
#         if bishop in range(board):
#             if bishop in (letters+-1 == numbers+-1):
#                 move()
#             elif pieceColor == color:
#                 print("Move was invalid, own piece already in square")
#             else:
#                 print("Move was invalid")


# def queenMove(queen):
#     for pieceColor in [Terminal.Color.DARKGREY, Terminal.Color.WHITE]:
#         if queen in range(board):
#             if queen in (letters+-1 == numbers+-1):
#                 move()
#             elif queen in range(len(letters)) or range(len(numbers)):
#                 move()
#             else:
#                 print("Move was invalid")

# def kingMove(king):
#     for pieceColor in [Terminal.Color.DARKGREY, Terminal.Color.WHITE]:
#         if king in range(board):
#             if king in (letters+-1 and numbers +-1):
#                 move()
#             else:
#                 print("Move was invalid")




# game loop
gameOver = False
loser = ''
while not gameOver:
    for color in ['black', 'white']:
        for row in board:
            for space in row:
                if not kingChr[color] in str(space):
                    
                    gameOver = True
                    # print('not found', color)

                    if color == 'white':
                        loser = Terminal.Color.WHITE + color + Terminal.Color.END
                    else:
                        loser = Terminal.Color.DARKGREY + color + Terminal.Color.END

                else:
                    # print('found')
                    gameOver = False
                    loser = ''
                    break
            if not gameOver:
                break
        

    if gameOver:
        print(f'{loser} lost')
        break
    

    # checking for valid move
    while True:
        # displays what color's turn it is
        print(f"{currColor}TURN{Terminal.Color.END}")

        # setup for asking what piece to move
        print('piece to move')
        pieceToMove = ['', '']
        executed = 0
        
        # loop to find the piece to move
        while True:
            executed = 0
            # ask what column letter they want, if that letter isn't a column letter, ask again
            while not (pieceToMove[0] in letters):
                if executed != 0:
                    Terminal.clearCurrLine() # puts the cursor back at the beginning of the line, so there is only one line for this query
                executed += 1
                pieceToMove[0] = Terminal.delayInput('column letter: ', delay).upper()
            
            executed = 0
            # ask what row number they want, if that number isn't a row number, ask again
            while not (pieceToMove[1] in numbers):
                if executed != 0:
                    Terminal.clearCurrLine() # puts the cursor back at the beginning of the line, so there is only one line for this query
                executed += 1
                pieceToMove[1] = Terminal.delayInput('row number: ', delay)
                
            
            # assign the list indeces to 
            pieceToMove = [numbers[pieceToMove[1]], letters[pieceToMove[0]]]

            # is the piece entered to be moved the same color as the current turn
            if currColor in str(board[pieceToMove[0]][pieceToMove[1]]):
                # stop asking for a piece to move
                break
            # remove the questions from above
            else:
                Terminal.clearCurrLine()
                Terminal.clearCurrLine()
                
                
                    
        # setup for asaking where to move it
        print('where to move it')
        posToMoveTo = ['', '']

        # ask what column letter they want, if that letter isn't a column letter, ask again
        executed = 0
        while not (posToMoveTo[0] in letters):
            if executed != 0:
                Terminal.clearCurrLine() # puts the cursor back at the beginning of the line, so there is only one line for this query
            executed += 1
            posToMoveTo[0] = Terminal.delayInput('column letter: ', delay).upper()
        
        # ask what column letter they want, if that letter isn't a column letter, ask again
        executed = 0
        while not (posToMoveTo[1] in numbers):
            if executed != 0:
                Terminal.clearCurrLine() # puts the cursor back at the beginning of the line, so there is only one line for this query
            executed += 1
            posToMoveTo[1] = Terminal.delayInput('row number: ', delay)


        # assign the desired location to move to as list indeces
        posToMoveTo = [numbers[posToMoveTo[1]], letters[posToMoveTo[0]]]
        
        # check if move is a valid move
        if board[pieceToMove[0]][pieceToMove[1]].canMove(pieceToMove, posToMoveTo, board):

            # turn change
            if currColor == Terminal.Color.WHITE:
                currColor = Terminal.Color.DARKGREY
            elif currColor == Terminal.Color.DARKGREY:
                currColor = Terminal.Color.WHITE
            


            board[pieceToMove[0]][pieceToMove[1]].move(pieceToMove, posToMoveTo, board)

            for row in board:
                row.reverse()
            board.reverse()

            Terminal.clear()
            print(Grid.build(board))
            break
        else:
            for i in range(7):
                Terminal.clearCurrLine()
    

    # move the piece
    # move(pieceToMove, posToMoveTo)