from typing import Dict, List, Any, Hashable


def displayGame():
    """
    Displays the welcome banner to the players
    """

    print('Welcome to the game of Tic Tac Toe')
    print('Author: SidyB')
    print('\n')
    print('Let\'s get ready to rumble!!!')
    print('#######################################')
    print('\n')

def gameOn(userInput: str) -> bool:
    """
    Determines if the user want to play/keep playing game.

    parameters:
    - userInput: Takes input of the user
    """
    on,off = ('Y', 'N')
    while isinstance(userInput, str) == False or userInput not in (on, off):
        userInput = input('Do you want to play the game? [Y/N]: ').upper()
        if userInput not in (on, off):
            print('Invalid input. Please enter Y or N')
    if userInput == on:
        return True
    elif userInput == off:
        return False

def startGame() -> bool:
    """
    Asks the user if they want to play the game and starts the game.
    """
    state = False
    while state == False:
        state = gameOn(input('Do you want to play the game? [Y/N]: ').upper())
    return state

def playerChoice() -> Dict[str, str]:
    """
    Prompts the user to enter their choice of marker (X or O)

    returns:
    - payerChoice: A dictionary containing the choice of the players
    """
    marker = ''
    players = {}
    while marker not in ('X', 'O'):
        marker = input('[Player 1]: Do you want to be X or O? ').upper()
        if marker not in ('X', 'O'):
            print('Invalid input. Please enter X or O')
            continue
    if marker == 'X':
        players['P1'] = 'X'
        players['P2'] = 'O'
    else:
        players['P1'] = 'O'
        players['P2'] = 'X'
    return dict(players)

def createBoard() -> List[List[str]]:
    """
    Askes the user to enter the size of the board and creates the board for the game.
    """
    boardSize = ''
    while boardSize.isnumeric() == False and boardSize not in range(3, 10):
        boardSize = input('Enter the size of the board [3-10]: ')
        
        if boardSize.isnumeric() == False and boardSize not in range(3, 10):
            print('Invalid input. Please enter a number between 3 and 10')
            continue
    boardSize = int(boardSize) 
    arrBoard = [['-' for i in range(boardSize)] for j in range(boardSize)]
    return arrBoard

def updateBoard(board: List[List[str]], marker: str, position: int) -> List[List[str]]:
    """
    Updates the board with the marker at the specified position.

    parameters:
    - board: The game board
    - marker: The marker to be placed on the board
    - position: The position on the board to place the marker
    """
    boardSize = len(board)
    row = (position-1) // boardSize
    col = (position-1) % boardSize
    print(row, col)
    if board[row][col] == '-':
        board[row][col] = marker
    return board

def displayBoard(board: List[List[str]]) -> None:
    """
    Displays the game board to the players
    """
    boardSize = len(board)
    print('-' * boardSize * 4)
    for i in range(boardSize):
        print('| ' + ' | '.join(board[i]) + ' |')
        if i < boardSize - 1:
            print('-' * boardSize * 4)
        elif i == boardSize - 1:
            print('-' * boardSize * 4)
    print('\n')

def displayPositions(board: List[List[str]]) -> None:
    """
    Displays the positions on the board to the players
    """
    boardSize = len(board)
    print('The positions on the board are as follows:')
    print('-' * boardSize * 5)
    for i in range(1, boardSize**2 + 1): # boardSize**2 + 1 to include the last position
        row = (i-1) // boardSize
        col = (i-1) % boardSize
        
        if board[row][col] == 'X' or board[row][col] == 'O':
            print(f'| {board[row][col]}', end=' ')

        elif i < boardSize**2 + 1:
            print(f'| {i:02}', end=' ') # f-string converts the integer to a string and adds a leading zero if the number is less than 10 for better readability
        else:
            print(f'| {i}', end=' ')
        
        if i % boardSize == 0:
            print('|\n' + '-' * boardSize * 5)


def checkWinner(board: List[List[str]], marker: str) -> bool:
    """
    Checks if the player has won the game

    parameters:
    - board: The game board
    - marker: The marker to be placed on the board
    """
    boardSize = len(board)

    for i in range(1, boardSize**2 + 1): # boardSize**2 + 1 to include the last position
        row = (i-1) // boardSize
        col = (i-1) % boardSize

        if board[row][col] == marker:
            # check for horizontal win
            for position in board[row][col+1:col+2]:
                if position == marker and col+2 < boardSize and board[row][col+2] == marker:
                    return True
            # check for vertical win
            for position in board[row+1:row+2]:
                if position[col] == marker and row+2 < boardSize and board[row+2][col] == marker: # row+2 < boardSize to avoid index out of range error
                    return True
            # check for diagonal win
            if board[row+1][col-1] == marker and board[row-1][col+1] == marker:
                return True
            elif board[row-1][col-1] == marker and board[row+1][col+1] == marker:
                return True
        else:
            continue
    return False
