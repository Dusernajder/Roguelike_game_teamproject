import util
import random

test_board = [['X', 'X', 'X', 'X', 'X'], ['1', '1', '1', '1', '1'], ['X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]
freespace = ' '
walls = 'X'
hero = util.read_table_from_file('hero.csv', ';')
monster = util.read_table_from_file('enemy.csv', ';')

monster_headers = ['ID','Name', 'Icon', 'HP', 'Attack', 'Deffense', 'Agility', 'Level','X','Y']
hero_headers = ['Name', 'Icon', 'HP', 'Attack', 'Deffense', 'Agility', 'Level']

monsters_dict = util.make_dict(monster, monster_headers)
hero_dict = util.make_dict(hero, hero_headers)


def max_monster_on_map(floorsize):
    return int(len(floorsize) * 0.2)


def pick_valid_places(board):
    valid_place = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == '1':
                valid_place.append((i, j))
    return valid_place


def pick_monster(monsters, player, monster_number_count):
    picked_monsters = []
    monsters_list = []
    for monster in monsters:
        monster_level = int(monster['Level'])
        player_level = int(player[0]['Level'])
        if monster_level == player_level or monster_level == player_level + 1 or monster_level == player_level - 1:
            monsters_list.append(monster)
    for i in range(monster_number_count):
        picked_monsters.append(random.choice(monsters_list))
    return picked_monsters


def monster_placement(validplace, monsters, board, monsters_alive):
    monster_left_to_place = monsters
    for monster in monster_left_to_place:
        monster['ID'] = util.generate_id()
    used = []
    for i in monster_left_to_place:
        if i not in used:
            place = random.choice(validplace)
            i['X'], i['Y'] = place[0], place[1]
            board[place[0]][place[1]] = i['Icon']
            monsters_alive.append(i['ID'])
            used.append(i)



def monster_movement(board, monsters_alive, monster_dict,valid_place):
    can_move = []

    current_monster = None
    for monster_id in range(len(monsters_alive)):
        for monster in monster_dict:
            if monsters_alive[monster_id] == monster['ID']:
                current_monster = monster
                possible_moves = []
                possible_moves.append((monster['X'] + 1,monster['Y'])), possible_moves.append((monster['X'] - 1,monster['Y']))
                possible_moves.append((monster['X'], monster['Y'] + 1)), possible_moves.append((monster['X'], monster['Y'] - 1))
                for valid_move in range(len(valid_place)):
                    for possible_mv in possible_moves:
                        if valid_place[valid_move] == possible_mv:
                            can_move.append(possible_mv)
        move = random.choice(can_move)
        board[current_monster['X']][current_monster['Y']] = 1
        board[move[0]][move[1]] = current_monster['Icon']






def main():
    monsters_alive = []
    board = test_board
    monsters_alive = []
    floorsize = pick_valid_places(board)
    max_monsters = max_monster_on_map(floorsize)
    enemys = pick_monster(monsters_dict, hero_dict, max_monsters)
    monster_placement(floorsize, enemys, board, monsters_alive)
    print(board)
    monster_movement(board,monsters_alive, monsters_dict,floorsize)
    print(board)


if __name__ == '__main__':
    main()
