import util
import engine
import ui
import enemy
from final import  final_choreography
import lore
import vlc

PLAYER_ICON = u"\u263B"
PLAYER_START_X = 3
PLAYER_START_Y = 3
playlist = ['The Misty Mountains Cold - The Hobbit.mp3' for _ in range(5)]

def create_player():
    return PLAYER_ICON


def main():
    for song in playlist:
        player = vlc.MediaPlayer(song)
        player.play()
    player = create_player()
    player_stats = lore.start_lore()
    board = engine.create_board()
    util.clear_screen()
    for i in range(3):
        board = engine.create_board()
        monsters_alive = []  # store the still alive monster ids
        floorsize = enemy.pick_valid_places(board)
        max_monsters = enemy.max_monster_on_map(floorsize)
        enemys = enemy.pick_monster(enemy.monsters_dict, enemy.hero_dict, max_monsters)
        enemy.monster_placement(floorsize, enemys, board, monsters_alive)
        engine.put_player_on_board(board, player,monsters_alive,enemy.monsters_dict,floorsize, player_stats)

    ui.display_board(board)
    util.clear_screen()
    final_choreography()


if __name__ == '__main__':
    main()
