from random import randint

game_is_over = False

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = randint(1, 2)


def choose_first():
    global player
    if player == 1:
        player = 'X'
    else:
        player = 'O'
    return player


def change_turn():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def play_the_game(player):
    print("The player " + player + " is turn now")
    print("the board is ")
    display_board(board)
    position = player_input(player)
    place_marker(board, player, position)
    win_check(board)
    change_turn()
    pass


def display_board(board):
    i = 0
    while i < len(board):
        if i == 2 or i == 5 or i == 8:
            print(board[i], end="\n")
        else:
            print(board[i], end="|")
        i += 1
    pass


def player_input(user):
    position = input("Your turn, " + user + " select the number")
    return position


def place_marker(board, marker, position):
    if check_if_is_number(position) and 1 <= int(position) <= 9:
        board[int(position) - 1] = marker

    else:
        print_error()


def check_if_is_number(position):
    try:
        int(position)
        return True
    except ValueError:
        return False


def win_check(board):
    global game_is_over
    if ((board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or  # across the top
            (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or  # across the middle
            (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or  # across the bottom
            (board[6] == 'X' and board[3] == 'X' and board[0] == 'X') or  # down the middle
            (board[7] == 'X' and board[4] == 'X' and board[1] == 'X') or  # down the middle
            (board[7] == 'X' and board[4] == 'X' and board[2] == 'X') or  # down the right side
            (board[6] == 'X' and board[4] == 'X' and board[2] == 'X') or  # diagonal
            (board[8] == 'X' and board[4] == 'X' and board[0] == 'X')):
        print('Player 1 is won')
        game_is_over = True


    elif ((board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or  # across the top
              (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or  # across the middle
              (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or  # across the bottom
              (board[6] == 'O' and board[3] == 'O' and board[0] == 'O') or  # down the middle
              (board[7] == 'O' and board[4] == 'O' and board[1] == 'O') or  # down the middle
              (board[8] == 'O' and board[5] == 'O' and board[2] == 'O') or  # down the right side
              (board[6] == 'O' and board[4] == 'O' and board[2] == 'O') or  # diagonal
              (board[8] == 'O' and board[4] == 'O' and board[0] == 'O')):
        print('Player 2 is won')
        game_is_over = True

    elif ((board[0] == 'X' or board[0] == 'O') and
              (board[1] == 'X' or board[1] == 'O') and
              (board[2] == 'X' or board[2] == 'O') and
              (board[3] == 'X' or board[3] == 'O') and
              (board[4] == 'X' or board[4] == 'O') and
              (board[5] == 'X' or board[5] == 'O') and
              (board[6] == 'X' or board[6] == 'O') and
              (board[7] == 'X' or board[7] == 'O') and
              (board[8] == 'X' or board[8] == 'O')):
        print('Count is draw')
        game_is_over = True
    else:
        pass


def print_error():
    print("You should choose correct position for your turn")
    pass


player = choose_first()

while game_is_over is not True:
    play_the_game(player)
else:
    print('The Game is over')
