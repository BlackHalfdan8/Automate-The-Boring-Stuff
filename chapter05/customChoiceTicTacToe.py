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

def playerMove(board, player):
    print('Turn for ' + player + '. Move on which space? Remaining spaces:', availableSpaces(board))
    move = input()
    while move not in availableSpaces(board):
        print("Invalid move! Choose from the remaining spaces:", availableSpaces(board))
        move = input()
    return move

def computerMove(board, player):
    return random.choice(availableSpaces(board))

def playTicTacToe():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    print("Welcome to Tic-Tac-Toe!")
    printBoard(theBoard)

    player_choice = input("Do you want to play against another human (H) or a computer (C)? ").upper()

    if player_choice == 'H':
        player1 = 'X'
        player2 = 'O'
        current_player = player1
        while True:
            move = playerMove(theBoard, current_player)
            theBoard[move] = current_player
            printBoard(theBoard)
            if checkWinner(theBoard, current_player):
                print('Player ' + current_player + ' wins!')
                break
            elif ' ' not in theBoard.values():
                print("It's a tie!")
                break
            current_player = player2 if current_player == player1 else player1

    elif player_choice == 'C':
        player = 'X'
        computer = 'O'
        current_player = player
        while True:
            if current_player == player:
                move = playerMove(theBoard, current_player)
            else:
                move = computerMove(theBoard, current_player)
            theBoard[move] = current_player
            printBoard(theBoard)
            if checkWinner(theBoard, current_player):
                if current_player == player:
                    print('Player ' + current_player + ' wins!')
                else:
                    print('Computer wins!')
                break
            elif ' ' not in theBoard.values():
                print("It's a tie!")
                break
            current_player = player if current_player == computer else computer

    else:
        print("Invalid choice. Please enter 'H' to play against another human or 'C' to play against a computer.")

playTicTacToe()
