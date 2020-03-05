import util
import engine
import ui

PLAYER_ICON = u"\u263B"
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    return PLAYER_ICON


def main():
    player = create_player()
    board = engine.create_board()

    util.clear_screen()

    engine.put_player_on_board(board, player)

    ui.display_board(board)
    util.clear_screen()


if __name__ == '__main__':
    main()
