from time import sleep
from util import read_table_from_file
import os


# def import_final_chars(file_name):
#     try:
#         with open(file_name, "r") as file:
#             lines = file.readlines()
#         return [element.replace("\n", "").split('\n') for element in lines]
#     except IOError:
#         pass


def start_position(boss, movement_type_one, move, warrior_distance, boss_text):
    boss_count = 48
    player_visibility = -8
    for h in range(10):
        sleep(0.2)
        os.system('clear')
        boss_count -= move
        warrior_distance -= move
        player_visibility += move
        for i in range(len(boss)):
            print(' '*boss_count + boss[i][0] + boss_text[i][0] + movement_type_one[i][0][:player_visibility*2])
            if h == 0:
                sleep(0.01)
    return warrior_distance


def move_R_L(boss, charachter, move, warrior_distance, direction, steps=1):
    for step in range(steps):
        if direction == 'L':
            warrior_distance -= move
        elif direction == 'R':
            warrior_distance += move
        view(boss, charachter, warrior_distance)
    return warrior_distance


def view(boss, charachter, warrior_distance, charachter_two=None, final=False):
    sleep(0.2)
    os.system('clear')
    if final:
        x = 0
        z = 11
        for h in range(17):
            x += 5
            z += 5
            os.system('clear')
            for i in range(len(charachter)):
                print(boss[i][0][x:len(boss[i][0])] + charachter[i][0][2:z] + charachter_two[i][0])
            sleep(0.05)
    else:
        for i in range(len(charachter)):
            print(boss[i][0] + ' '*warrior_distance + charachter[i][0])


def final_choreography():
    warrior_distance = 98
    move = 8
    fast_move = 32
    charachters = {}
    get_ch = charachters.get

    charachters['boss'] = read_table_from_file('final_boss/boss.txt', '\n')
    charachters['movement_type_one'] = read_table_from_file('final_boss/fight_one.txt', '\n')
    charachters['movement_type_two'] = read_table_from_file('final_boss/fight_two.txt', '\n')
    charachters['movement_type_three'] = read_table_from_file('final_boss/fight_three.txt', '\n')
    charachters['movement_type_four'] = read_table_from_file('final_boss/fight_four.txt', '\n')
    charachters['boss_text'] = read_table_from_file('final_boss/youshallnotpass.txt', '\n')
    charachters['execute'] = read_table_from_file('final_boss/execute.txt', '\n')

    warrior_distance = start_position(get_ch('boss'), get_ch('movement_type_one'), move, warrior_distance, get_ch('boss_text'))
    warrior_distance = move_R_L(get_ch('boss'), get_ch('movement_type_two'), fast_move, warrior_distance, 'L')
    warrior_distance = move_R_L(get_ch('boss'), get_ch('movement_type_one'), fast_move, warrior_distance, 'R', 2)
    view(get_ch('boss'), get_ch('movement_type_two'), warrior_distance)
    view(get_ch('boss'), get_ch('movement_type_one'), warrior_distance)
    view(get_ch('boss'), get_ch('movement_type_two'), warrior_distance)
    warrior_distance = move_R_L(get_ch('boss'), get_ch('movement_type_one'), move, warrior_distance, 'L', 3)
    view(get_ch('boss'), get_ch('movement_type_two'), warrior_distance)
    view(get_ch('boss'), get_ch('movement_type_three'), warrior_distance)
    sleep(0.5)
    warrior_distance = move_R_L(get_ch('boss'), get_ch('movement_type_four'), move, warrior_distance, 'L')
    view(get_ch('boss'), get_ch('execute'), warrior_distance, get_ch('movement_type_four'), True)


def main():
    final_choreography()


if __name__ == '__main__':
    main()
