theBoard = {
    "Top-l":'',
    "Top-m":'',
    "Top-r":'',
    "Mid-l":'',
    "Mid-m":'',
    "Mid-r":'',
    "Low-l":'',
    "Low-m":'',
    "Low-r":''
}

def printBoard(board):
    print(board["Top-l"] + "|" + board["Top-m"] + "|" + board["Top-r"])
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print(board["Mid-l"] + "|" + board["Mid-m"] + "|" + board["Mid-r"])
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print(board["Low-l"] + "|" + board["Low-m"] + "|" + board["Low-r"])

turn = 'x'  
for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    theBoard[move] = turn

    if turn == 'x': 
        turn = 'O'  
    else:
        turn = 'X'  
printBoard(theBoard) 
