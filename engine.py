import map as gmap
import util
import numpy as np
import time


def create_board():
    '''
    Creates a new game board based on input parameters.

    Returns:
    list: Game board
    '''
    return gmap.get_random_map()


def place_player(board, player):
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if board[row_index][cell_index] == ' ':
                board[row_index][cell_index] = player
                break
            break


def find_last_gate(board):
    last_column = 49
    for i in range(last_column):
        if board[i][49] == " ":
            return i


def next_map(board, player):
    if board[find_last_gate(board)][len(board)-1] == player:
        return True


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()


def move_right(board, previous_spot, height, width, player_position):
    if player_position[1] != len(board) - 1 and board[height][width] != 'X':
        test_player_position = player_position[:]
        test_player_position[1] += 1
        test_height = test_player_position[0]
        test_width = test_player_position[1]

        if board[test_height][test_width] != 'X':
            board[height][width] = previous_spot
            player_position[1] += 1
            height = player_position[0]
            width = player_position[1]
            previous_spot = board[height][width]


def move_left(board, previous_spot, height, width, player_position):
    if player_position[1] != 0 and board[height][width] != 'X':
        test_player_position = player_position[:]
        test_player_position[1] -= 1
        test_height = test_player_position[0]
        test_width = test_player_position[1]

        if board[test_height][test_width] != 'X':
            board[height][width] = previous_spot
            player_position[1] -= 1
            height = player_position[0]
            width = player_position[1]
            previous_spot = board[height][width]


def move_up(board, previous_spot, height, width, player_position):
    if player_position[0] != 0 and board[height][width] != 'X':
        test_player_position = player_position[:]
        test_player_position[0] -= 1
        test_height = test_player_position[0]
        test_width = test_player_position[1]

        if board[test_height][test_width] != 'X':
            board[height][width] = previous_spot
            player_position[0] -= 1
            height = player_position[0]
            width = player_position[1]
            previous_spot = board[height][width]


def move_down(board, previous_spot, height, width, player_position):
    if player_position[0] != len(board[0]) - 1 and board[height][width] != 'X':
        test_player_position = player_position[:]
        test_player_position[0] += 1
        test_height = test_player_position[0]
        test_width = test_player_position[1]

        if board[test_height][test_width] != 'X':
            board[height][width] = previous_spot
            player_position[0] += 1
            height = player_position[0]
            width = player_position[1]
            previous_spot = board[height][width]


def put_player_on_board(board, player):
    place_player(board, player)
    previous_spot = ' '
    while True:
        time.sleep(0.05)
        util.clear_screen()
        print_board(board)
        key = util.key_pressed()
        player_position = [np.where(board == player)[0][0], np.where(board == player)[1][0]]
        height = player_position[0]
        width = player_position[1]

        if key == 'd':
            move_right(board, previous_spot, height, width, player_position)
        elif key == 'a':
            move_left(board, previous_spot, height, width, player_position)
        elif key == 'w':
            move_up(board, previous_spot, height, width, player_position)
        elif key == 's':
            move_down(board, previous_spot, height, width, player_position)
        elif key == 'q':
            break

        try:
            if next_map(board, player):
                break
        except:
            break


        height = player_position[0]
        width = player_position[1]
        board[height][width] = player

    return board

