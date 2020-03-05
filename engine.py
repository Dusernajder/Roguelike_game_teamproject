import map as gmap
import util
import numpy as np

def create_board():
    '''
    Creates a new game board based on input parameters.

    Returns:
    list: Game board
    '''
    return gmap.get_random_map()


def place_player(board):
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if board[row_index][cell_index]==' ':
                board[row_index][cell_index]='@'
                break
            break


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()


def put_player_on_board(board, player):
    place_player(board)
    previous_spot = ' '
    while True:
        print_board(board)

        key = util.key_pressed()
        player_position = [np.where(board == '@')[0][0], np.where(board == '@')[1][0]]

        height = player_position[0]
        width = player_position[1]
        if key == 'd':
            if player_position[1] != len(board)-1:
                board[height][width] = previous_spot
                player_position[1] += 1
                height = player_position[0]
                width = player_position[1]
                previous_spot = board[height][width]
        elif key == 'a':
            if player_position[1] != 0:
                board[height][width] = previous_spot
                player_position[1] -= 1
                height = player_position[0]
                width = player_position[1]
                previous_spot = board[height][width]
        elif key == 'w':
            if player_position[0] != 0:
                board[height][width] = previous_spot
                player_position[0] -= 1
                height = player_position[0]
                width = player_position[1]
                previous_spot = board[height][width]
        elif key == 's':
            if player_position[0] != len(board[0])-1:

                board[height][width] = previous_spot
                player_position[0] += 1
                height = player_position[0]
                width = player_position[1]
                previous_spot = board[height][width]
        elif key == 'q':
            break

        height = player_position[0]
        width = player_position[1]
        board[height][width] = player

    return board


put_player_on_board(create_board(), '@')
