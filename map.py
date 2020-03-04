import random
import numpy as np

shape = (20, 20)
WALL = 0
FLOOR = 1
fill_prob = 0.32
generations = 6


def generate_random_map(new_map):
    for i in range(shape[0]):
        for j in range(shape[1]):
            choice = random.uniform(0, 1)
            new_map[i][j] = WALL if choice < fill_prob else FLOOR
    return new_map


def display_matrix(matrix):
    line = ''
    for i in range(shape[0]):
        for j in range(shape[1]):
            line += ' #  ' if matrix[i][j] == WALL else ' .  '
        print(line)
        line = ''


def generate_map(new_map, shape):
    for generation in range(generations):
        for i in range(shape[0]):
            for j in range(shape[1]):
                submap = new_map[max(i - 1, 0):min(i + 2, new_map.shape[0]), max(j - 1, 0):min(j + 2, new_map.shape[1])]
                wallcount_1away = len(np.where(submap.flatten() == WALL)[0])
                submap = new_map[max(i - 2, 0):min(i + 3, new_map.shape[0]), max(j - 2, 0):min(j + 3, new_map.shape[1])]
                wallcount_2away = len(np.where(submap.flatten() == WALL)[0])

                if wallcount_1away >= 5 or wallcount_2away <= 7:
                    new_map[i][j] = WALL
                else:
                    new_map[i][j] = FLOOR
                if i == 0 or j == 0 or i == shape[0] - 1 or j == shape[1] - 1:
                    new_map[i][j] = WALL

    return new_map


# Getter - Setter

def set_map_size(x, y):
    shape = [x, y]


if __name__ == '__main__':
    new_map = np.ones((shape), dtype = int)
    new_map = generate_random_map(new_map)
    display_matrix(generate_map(new_map, shape))
