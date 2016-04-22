def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    if board['top-L'] == player and board['top-M'] == player and board['top-R'] == player:
        return True
    elif board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player:
        return True
    elif board['low-L'] == player and board['low-M'] == player and board['low-R'] == player:
        return True
    elif board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player:
        return True
    elif board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player:
        return True
    elif board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player:
        return True
    elif board['top-L'] == player and board['mid-M'] == player and board['low-L'] == player:
        return True
    elif board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player:
        return True
    else:
        return False
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #Makes the startingPlayer to be the first
    for i in range(9):    #Makes a loop for when i is in range 9
        printBoard(board) #Prints the board
        print('Turn for ' + turn + '. Move on which space?') #On your turn, print 'Turn for " ". Move on which space?'
        move = input()    #Their move
        board[move] = turn#Updates board of player's move
        if( checkWinner(board, 'X') ):#calls checkWinner function to see if play X or O wins. If so, stop the game.
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):
            print('O wins!')
            break
    
        if turn == 'X': #Swap turns. 
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
