import util
import engine
import ui
from final import  final_choreography


PLAYER_ICON = u"\u263B"
PLAYER_START_X = 3
PLAYER_START_Y = 3


def choose_class():
	for i, x in enumerate(['Warrior', 'Mage', 'Thief']):
		print(f'{i} {x}')
	choice = input('Choose class:')
	if choice == '0':
		return {'Name': 'Warrior', 'Hp': 20, 'Attack': 10, 'Defense': 15, 'Agility': 5, 'Level': 1}
	elif choice == '1':
		return {'Name': 'Mage', 'Hp': 15, 'Attack': 15, 'Defense': 5, 'Agility': 10, 'Level': 1}
	elif choice == '2':
		return {'Name': 'Thief', 'Hp': 10, 'Attack': 15, 'Defense': 5, 'Agility': 20, 'Level': 1}


def create_player():
    return PLAYER_ICON


def main():

    player = create_player()
    player_stats = choose_class()
    #printLore
    board = engine.create_board()

    util.clear_screen()
    for i in range(3):
        board = engine.create_board()
        engine.put_player_on_board(board, player)

    ui.display_board(board)
    util.clear_screen()
    final_choreography()


if __name__ == '__main__':
    main()
