import util
import random
import numpy as np
import engine
import main
import time

hero = util.read_table_from_file('hero.csv', ';')
monster = util.read_table_from_file('enemy.csv', ';')

monster_headers = ['ID', 'Name', 'Icon', 'HP', 'Attack', 'Deffense', 'Agility', 'Level', 'X', 'Y']
hero_headers = ['Name', 'Icon', 'HP', 'Attack', 'Deffense', 'Agility', 'Level']

monsters_dict = util.make_dict(monster, monster_headers)
hero_dict = util.make_dict(hero, hero_headers)


def max_monster_on_map(floorsize):  # chose the maximum number of monster on the given map
    return int(len(floorsize) * 0.2)


def pick_valid_places(board):  # check valid places to place or move
    valid_place = []
    for i in range(50):
        for j in range(50):
            if board[i][j] == ' ':
                valid_place.append((i, j))
    return valid_place


def pick_monster(monsters, player,
                 monster_number_count):  # pick monsters from the monsters dictionary for the player level
    picked_monsters = []
    monsters_list = []
    for monster in monsters:
        monster_level = int(monster['Level'])
        player_level = int(player[0]['Level'])
        if monster_level == player_level or monster_level == player_level + 1 or monster_level == player_level - 1:
            monsters_list.append(monster)
    for count in range(monster_number_count):
        picked_monsters.append(random.choice(monsters_list))
    return picked_monsters


def monster_placement(validplace, monsters, board, monsters_alive):  # place the chosen monsters
    monster_left_to_place = monsters
    used = []
    for monster in monster_left_to_place:
        monster['ID'] = util.generate_id()

    for monster_dict in monster_left_to_place:
        if monster_dict not in used:
            place = random.choice(validplace)
            monster_dict['X'], monster_dict['Y'] = place[0], place[1]

            board[place[0]][place[1]] = monster_dict['Icon']

            monsters_alive.append(monster_dict)
            used.append(monster_dict)


def monster_movement(board, monsters_alive, valid_place):  # when you call it it moves all the 'living' monsters
    for monster in monsters_alive:
        possible_moves = []

        append = possible_moves.append
        append((monster['X'] + 1, monster['Y'])), append((monster['X'] - 1, monster['Y']))
        append((monster['X'], monster['Y'] + 1)), append((monster['X'], monster['Y'] - 1))

        can_move = [x for x in possible_moves if x in valid_place]

        move = random.choice(can_move)

        board[monster['X']][monster['Y']] = ' '
        monster['X'], monster['Y'] = move[0], move[1]
        board[int(monster['X'])][int(monster['Y'])] = monster['Icon']


def trigger_fight(player, board, monsters_alive):
    player = main.create_player()
    current_monster = None
    for monster in monsters_alive:
        current_monster = monster
        for x in board:
            for y in x:
                if board[x][y] == player and monster['X'],monster['Y']:

        if monster[] == player:
            print('KEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKE')
            time.sleep(2)



