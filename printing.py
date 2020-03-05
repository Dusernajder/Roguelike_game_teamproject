
# def get_lore_entry(player_class):
	


# def print_lore(player_class):
	


def join_tables(table_one, table_two):
	max_len = max([len(table_one), len(table_two)])
	full_table = [f'{table_one[i]}  {table_two[i]}' for i in range(max_len)]
	return full_table

def get_max_width(data, values=None):
	if values:
		return len(max([str(value) for key, value in data.items()], key=len))
	return len(max(data.keys(), key=len))


def create_table_content(character_stats):
	headers = ['Name', 'Hp', 'Attack', 'Defense', 'Agility', 'Level']
	keys_max_len = get_max_width(character_stats) + 2
	values_max_len = get_max_width(character_stats, values=True) + 2
	blocks = [f'│{key.center(keys_max_len)}│{str(val).center(values_max_len)}│' for key, val in character_stats.items() if key in headers]
	max_len = len(max(blocks, key=len)) -2
	blocks.insert(0, '┌' + '─' * max_len + '┐')
	blocks.append('└' + '─' * max_len + '┘')
	return blocks


def print_tables(player, enemy, max_width):
	player_table = create_table_content(player)
	enemy_table = create_table_content(enemy)
	joined_table = join_tables(player_table, enemy_table)
	[print(x.center(max_width)) for x in joined_table]


def print_board(width, length):
	space = ' ' * width
	board = [f'│{space}│' for _ in range(length)]
	board.insert(0, '┌' + '─' * width + '┐')
	board.append('└' + '─' * width + '┘')
	[print(row) for row in board]


def create_textbox(mssg):
	textbox = [f'│ {mssg} │']
	textbox.insert(0, '┌' + '─' * (len(mssg)+2) + '┐')
	textbox.append('└' + '─' * (len(mssg)+2) + '┘')
	return textbox



def print_mssg(mssg, width):
	textbox = create_textbox(mssg)
	[print(x.center(width)) for x in textbox]



def print_fight_board(player, enemy, mssg=None):
	board_width = 120
	board_length = 25
	print_board(board_width, board_length)
	if mssg:
		print_mssg(mssg, board_width)
	print_tables(player, enemy, board_width)


# if __name__ == '__main__':
# 	print_fight_board({'Name': 'Joe', 'Hp': 20, 'Attack': 10, 'Defense': 15, 'Agility': 5, 'Level': 1, 'Exp': 0}, {'Name': 'Orc', 'Hp': 15, 'Attack': 10, 'Defense': 10, 'Agility': 10, 'Level': 1}, mssg='Warrior Dodged!')
	


