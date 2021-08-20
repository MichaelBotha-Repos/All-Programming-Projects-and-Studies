# SCENARIO
# Program uses x's
# User uses O's
# PC makes first move - placing in middle of board
# All squares all numbered row by row starting with 1 i.e. 1-3 in first row
# user inputs their move by entering the number of the square to place x in -> the value must be valid 
# the position cannot already be occupied
# the program checks if the game is over -> there are 4 possible verdicts: continue, tie, PC win, user win 

# REQUIREMENTS
# Board should be stored as 3-element list containing a 3-element list in each element
# squares will be accessed via board[row][column]
# each of the inner list's elments can contain a O or X or number representing the blocks number = free 
# block

# a random integer can be drawn by using the randrange() function e.g 
#from random import randrange
#for i in range(10):
#   print(randrange(8))
# the from-import instruction provides access to the randrange function defined in the external Python
# module called random 

from random import randrange


def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console

    
    
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[0][0],'  |  ',board[0][1],'  |  ',board[0][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[1][0],'  |  ',board[1][1],'  |  ',board[1][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[2][0],'  |  ',board[2][1],'  |  ',board[2][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

    

def EnterMove(board):

# the function accepts the boards current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision

    while True:
        move = input('Please enter the number of the block to place your "O", or stop to exit\n')
        if move == '1':
            if board[0][0]== move:
                board[0][0]= "O"
                break
            else:
                print('not a valid entry') 
        elif move == '2':
            if board[0][1]== move:
                board[0][1]= "O"
                break
            else:
                print('not a valid entry')
        elif move == '3':
            if board[0][2]== move:
                board[0][2]= "O"
                break
            else:
                print('not a valid entry') 
        elif move == '4':
            if board[1][0]== move:
                board[1][0]= "O"
                break
            else:
                print('not a valid entry')
        elif move == '5':
            if board[1][1]== move:
                board[1][1]= "O"
                break
            else:
                print('not a valid entry')
        elif move == '6':
            if board[1][2]== move:
                board[1][2]= "O"
                break
            else:
                print('not a valid entry')
        elif move == '7':
            if board[2][0]== move:
                board[2][0]= "O"
                break
            else:
                print('not a valid entry')
        elif move == '8':
            if board[2][1]== move:
                board[2][1]= "O"
                break
            else:
                print('not a valid entry')
        elif move == '9':
            if board[2][2]== move:
                board[2][2]= "O"
                break
            else:
                print('not a valid entry')
        elif move == 'stop':
            break


        
#def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game

    if (sign == board[0][0])&(board[0][0]== board[0][1]) & (board[0][1]== board[0][2]):
        return True
    elif (sign == board[1][0])&(board[1][0]== board[1][1]) & (board[1][1]== board[1][2]):
        return True
    elif (sign == board[2][0])&(board[2][0]== board[2][1]) & (board[2][1]== board[2][2]):
        return True
    elif (sign == board[0][0])&(board[0][0]== board[1][0]) & (board[1][0]== board[2][0]):
        return True 
    elif (sign == board[0][1])&(board[0][1]== board[1][1]) & (board[1][1]== board[2][1]):
        return True 
    elif (sign == board[0][2])&(board[0][2]== board[1][2]) & (board[1][2]== board[2][2]):
        return True
    elif (sign == board[0][0])&(board[0][0]== board[1][1]) & (board[1][1]== board[2][2]):
        return True 
    elif (sign == board[0][2])&(board[0][2]== board[1][1]) & (board[1][1]== board[2][0]):
        return True
    else:
        return False


def DrawMove(board):
# the function draws the computer's move and updates the board
    x=1
    while x < 6:
        move = str(randrange(1,9))
        if move == '1':
            if board[0][0]== move:
                board[0][0]= "X"
                break
            else:
                continue 
        elif move == '2':
            if board[0][1]== move:
                board[0][1]= "X"
                break
            else:
                continue
        elif move == '3':
            if board[0][2]== move:
                board[0][2]= "X"
                break
            else:
                continue 
        elif move == '4':
            if board[1][0]== move:
                board[1][0]= "X"
                break
            else:
                continue
        elif move == '5':
            if board[1][1]== move:
                board[1][1]= "X"
                break
            else:
                continue
        elif move == '6':
            if board[1][2]== move:
                board[1][2]= "X"
                break
            else:
                continue
        elif move == '7':
            if board[2][0]== move:
                board[2][0]= "X"
                break
            else:
                continue
        elif move == '8':
            if board[2][1]== move:
                board[2][1]= "X"
                break
            else:
                continue
        elif move == '9':
            if board[2][2]== move:
                board[2][2]= "X"
                break
            else:
                continue
#End of functions

#Beginning of main body
board1= [['1','2','3'],['4','X','6'],['7','8','9']]
num = 0

while (VictoryFor(board1,'X')or VictoryFor(board1,'O')) != True:
    DisplayBoard(board1)
    EnterMove(board1)
    DrawMove(board1)
    num +=1
    if num == 4:
        break


if VictoryFor(board1,'X') == True:
    print('You lose')
elif VictoryFor(board1,'O')== True:
    print('You win')
else:
    print('draw')

