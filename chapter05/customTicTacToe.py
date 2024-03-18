theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):
    # Check rows
    for row in ['top', 'mid', 'low']:
        if board[row + '-L'] == board[row + '-M'] == board[row + '-R'] == player:
            return True
    # Check columns
    for col in ['L', 'M', 'R']:
        if board['top-' + col] == board['mid-' + col] == board['low-' + col] == player:
            return True
    # Check diagonals
    if board['top-L'] == board['mid-M'] == board['low-R'] == player:
        return True
    if board['top-R'] == board['mid-M'] == board['low-L'] == player:
        return True
    return False

def availableSpaces(board):
    return [space for space, value in board.items() if value == ' ']

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space? Remaining spaces:', availableSpaces(theBoard))
    move = input()
    while move not in availableSpaces(theBoard):
        print("Invalid move! Choose from the remaining spaces:", availableSpaces(theBoard))
        move = input()
    theBoard[move] = turn
    if checkWinner(theBoard, turn):
        printBoard(theBoard)
        print('Player ' + turn + ' wins!')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printBoard(theBoard)
    print("It's a tie!")
