import random
print("Below is the code for")
print("Designing the tic tac toe Python 3X3 grid gameboard of tic tac toe Python")
winner=None
CurrentPlayer="X"
GameRunning=True

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def printBoard(board):
    print(board[0]+ "|" +board[1]+ "|" +board[2])
    print("-------")

    print(board[3]+"|" +board[4]+ "|" +board[5])
    print("-------")
    print(board[6]+"|" +board[7]+ "|" +board[8])
    print("-------")

#take player input
def playergame(board):
    user=int(input("enter any number between 1 to 9: "))
    if user>=1 and user<=9 and board[user-1] =="-":
        board[user-1]=CurrentPlayer
    else:
        print("OOPS....")

#check win or tie
def CheckHorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[1]
        return True
    elif board[3]==board[4]==board[5] and board[2]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[8]!="-":
        winner=board[7]
        return True

def checkVertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[3]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[4]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[6]=="-":
        winner=board[2]
        return True

def checkTie(board):
    global GameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie..")
        GameRunning=False

def checkWin():
    global winner
    if CheckHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        print(f"The winner is {winner}")

#switch the player
def switchPlayer():
    global CurrentPlayer
    if CurrentPlayer=="X":
        CurrentPlayer="O"
    else:
        CurrentPlayer="X"
#computer
def computer(board):
    while CurrentPlayer=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchPlayer()

#check for win or tie again
while GameRunning:
    printBoard(board)
    playergame(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
















        


