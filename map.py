import random
import numpy as np

WALL = 'X'
FLOOR = ' '

shape = (50, 50)
fill_prob = 0.32
generations = 6


def generate_random_map(matrix):
    for i in range(shape[0]):
        for j in range(shape[1]):
            choice = random.uniform(0, 1)
            matrix[i][j] = WALL if choice < fill_prob else FLOOR
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(*row)


def generate_map(new_map, shape):
    for generation in range(generations):
        for i in range(shape[0]):
            for j in range(shape[1]):

                submap = new_map[max(i - 1, 0):min(i + 2, shape[0]), max(j - 1, 0):min(j + 2, shape[1])]
                wallcount_1away = len(np.where(submap.flatten('F') == WALL)[0])
                submap = new_map[max(i - 2, 0):min(i + 3, shape[0]), max(j - 2, 0):min(j + 3, shape[1])]
                wallcount_2away = len(np.where(submap.flatten('F') == WALL)[0])

                if wallcount_1away >= 5 or wallcount_2away <= 7:
                    new_map[i][j] = WALL
                else:
                    new_map[i][j] = FLOOR
                if i == 0 or j == 0 or i == shape[0] - 1 or j == shape[1] - 1:
                    new_map[i][j] = WALL

    return insert_doors(new_map)


def insert_doors(matrix):
    door_in, door_out = generate_door(matrix)

    for i in range(shape[0]):
        if matrix[door_in[0]][i] == 'X':
            matrix[door_in[0]][i] = ' '
        else:
            break

    for j in range(shape[0] - 1, 0, -1):
        if matrix[door_out[0]][j] == 'X':
            matrix[door_out[0]][j] = ' '
        else:
            break

    return matrix

def generate_door(matrix):
    door_in = []
    door_out = []

    label = False

    for i in range(shape[0]):
        if label:
            break
        for j in range(shape[1]):
            c1 = str(matrix[j][i])
            if c1 is ' ':
                door_in = (j, 0)
                label = True
                break

    label = False

    for x in range(shape[0] - 1, 0, -1):
        if label:
            break
        for y in range(shape[1] - 1, 0, -1):
            c2 = str(matrix[y][x])
            if c2 is ' ':
                door_out = (y, shape[1] - 1)
                label = True
                break

    return door_in, door_out


def place_treasure(matrix):


    pass



def get_random_map():
    new_map = np.ones((shape), dtype = str)
    m = generate_map(generate_random_map(new_map), shape)

    return m
