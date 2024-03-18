import random

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

def computerMove(board, player):
    return random.choice(availableSpaces(board))

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

player = 'X'
computer = 'O'

for i in range(9):
    printBoard(theBoard)
    if player == 'X':
        print('Turn for ' + player + '. Move on which space? Remaining spaces:', availableSpaces(theBoard))
        move = input()
        while move not in availableSpaces(theBoard):
            print("Invalid move! Choose from the remaining spaces:", availableSpaces(theBoard))
            move = input()
        theBoard[move] = player
    else:
        move = computerMove(theBoard, computer)
        theBoard[move] = player

    if checkWinner(theBoard, player):
        printBoard(theBoard)
        print('Player ' + player + ' wins!')
        break
    
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
else:
    printBoard(theBoard)
    print("It's a tie!")
