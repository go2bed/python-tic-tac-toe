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
    win_check(board, player)
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
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split():
        position = input("Your turn, " + user + " select the number between 1 and 9").strip()
    return int(position)


def place_marker(board, marker, position):
    if not check_if_is_number(board[position - 1]):
        player_input(marker)
    else:
        board[int(position) - 1] = marker


def check_if_is_number(position):
    try:
        int(position)
        return True
    except ValueError:
        print_error()
        return False


def win_check(board, player):
    global game_is_over
    if ((board[6] == board[7] == board[8] == player) or  # across the top
            (board[3] == board[4] == board[5] == player) or  # across the middle
            (board[0] == board[1] == board[2] == player) or  # across the bottom
            (board[6] == board[3] == board[0] == player) or  # down the middle
            (board[7] == board[4] == board[1] == player) or  # down the middle
            (board[7] == board[4] == board[2] == player) or  # down the right side
            (board[6] == board[4] == board[2] == player) or  # diagonal
            (board[8] == board[4] == board[0] == player)):
        print("Player " + player + " is won")
        replay()

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
        replay()
    else:
        pass


def print_error():
    print("You should choose correct position for your turn")
    pass


def replay():
    global board, game_is_over
    answer = input("Do you want to play again? Y/N").upper().strip()
    if answer == 'Y' or answer.upper().startswith('Y'):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        choose_first()
        game_is_over = False
    elif answer == 'N' or answer.upper().startswith('N'):
        game_is_over = True


player = choose_first()

while game_is_over is not True:
    play_the_game(player)
else:
    print('The Game is over')
