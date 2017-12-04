game_is_over = False

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def play_the_game():
    print("the board is ")
    display_board(board)
    player_choice = player_input()
    print("your choice is: " + player_choice)
    win_check()
    pass


def display_board(board):
    for i in board:
        if i % 3 == 0:
            print(i, end="\n")
        else:
            print(i, end="|")
    pass


def player_input():
    s = input("your turn, select the number")
    return s

def place_marker(board, marker, position):
    pass


def win_check(board, mark):
    global game_is_over
    game_is_over = True
    pass


while game_is_over is not True and board.__sizeof__() != 0:
    play_the_game()
else:
    print('The Game is over')
