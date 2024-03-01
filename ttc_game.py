import modules.game_funcs as game

def main():
    game.displayGame()
    players = game.playerChoice()
    player1 = players['P1']
    player2 = players['P2']
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
    
    winner = False
    while winner == False:
        p1move = game.playerMove(board, player1)
        game.updateBoard(board, player1, p1move)
        winner = game.checkWinner(board, player1)
        p2move = game.playerMove(board, player2)
        game.updateBoard(board, player2, p2move)
        winner = game.checkWinner(board, player2)
        continue
    print(winner)

    # if start == False:
    #     print('Goodbye!!!')
    #     return
    # elif start == True:
    #     print('Alright, let\'s play!!!')
    #     print('\n')









if __name__ == "__main__":
    main()