game_is_over = False

board = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def play_the_game():
    global game_is_over
    print(board)
    s = input("select your")
    game_is_over = True
    pass


while game_is_over is not True and board.__sizeof__() != 0:
    play_the_game()
else:
    print('The Game is over')
