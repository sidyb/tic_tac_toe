import modules.game_funcs as game

def main():
    game.displayGame()
    game.playerChoice()
    start = game.startGame()
    if start == False:
        print('Goodbye!!!')
        return
    elif start == True:
        print('Alright, let\'s play!!!')
        print('\n')
    board = game.createBoard()

    print(f'This is your Board')
    print('\n')
    game.displayBoard(board)
    print('\n')







if __name__ == "__main__":
    main()