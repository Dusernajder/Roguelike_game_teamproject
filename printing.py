
def join_tables(table_one, table_two):
	max_len = max([len(table_one), len(table_two)])
	full_table = [f'{table_one[i]}  {table_two[i]}' for i in range(max_len)]
	return full_table

def get_max_width(data, values=None):
	if values:
		return len(max([str(value) for key, value in data.items()], key=len))
	return len(max(data.keys(), key=len))


def make_table_content(character_stats):
	headers = ['Name', 'Hp', 'Attack', 'Defense', 'Agility', 'Level']
	keys_max_len = get_max_width(character_stats) + 2
	values_max_len = get_max_width(character_stats, values=True) + 2
	blocks = [f'│{key.center(keys_max_len)}│{str(val).center(values_max_len)}│' for key, val in character_stats.items() if key in headers]
	max_len = len(max(blocks, key=len)) -2
	blocks.insert(0, '┌' + '─' * max_len + '┐')
	blocks.append('└' + '─' * max_len + '┘')
	return blocks


def print_board(player, enemy):
	player_table = make_table_content(player)
	enemy_table = make_table_content(enemy)
	joined_table = join_tables(player_table, enemy_table)
	[print(x) for x in joined_table]






print_board({'Name': 'Joe', 'Hp': 20, 'Attack': 10, 'Defense': 15, 'Agility': 5, 'Level': 1, 'Exp': 0}, {'Name': 'Orc', 'Hp': 15, 'Attack': 10, 'Defense': 10, 'Agility': 10, 'Level': 1})