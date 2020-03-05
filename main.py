import util
import engine
import ui
from final import  final_choreography

PLAYER_ICON = u"\u263B"
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    return PLAYER_ICON


def main():

    player = create_player()

    util.clear_screen()
    for i in range(3):
        board = engine.create_board()
        engine.put_player_on_board(board, player)

    ui.display_board(board)
    util.clear_screen()
    final_choreography()


if __name__ == '__main__':
    main()
