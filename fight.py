from random import randint
import printing
import util


def not_dead(player, enemy):
	if player['Hp'] > 0 and enemy['Hp'] > 0:
		return True
	return False


def throw_six_sided_dice(n=1):
	return sum([randint(1, 6) for _ in range(n)])


def calculate_damage(attack, defense, agility):
	if agility >= randint(1,100): #calculate dodge chance
		return 0
	return attack - defense


def _turn_(attacker, defender, dice_number, player, enemy):
	att_name = attacker['Name']
	def_name = defender['Name']
	send_message(f'{att_name} throw with {dice_number} dice!', player, enemy)
	attack = throw_six_sided_dice(2)
	send_message(f'{att_name} throw {attack}!', player, enemy)
	send_message(f'{def_name} throw with {dice_number} dice!', player, enemy)
	defense = throw_six_sided_dice(2)
	send_message(f'{def_name} throw {defense}!', player, enemy)
	return calculate_damage(attacker['Attack']+attack, defender['Defense']+defense, defender['Agility'])


def get_message(damage, attacker, defender):
	if damage <= 0:
		name = defender['Name']
		return f'{name} dodged the attack!'
	else:
		name = attacker['Name']
		return f'{name} caused {damage} point(s) of damage!'
		

def send_message(message, player, enemy):
	util.clear_screen()
	printing.print_fight_board(player=player, enemy=enemy, mssg=message)
	input('Press Enter!')


def fight(player_stats, enemy):
	dice_number = 2
	player_name = player_stats['Name']
	enemy_name = enemy['Name']
	util.clear_screen()
	printing.print_fight_board(player_stats, enemy)
	message = None
	turn = 1
	while not_dead(player_stats, enemy):
		if turn % 2 != 0:
			damage = _turn_(player_stats, enemy, dice_number, player=player_stats, enemy=enemy)
			message = get_message(damage, player_stats, enemy)
			if damage > 0:
				enemy['Hp'] -= damage
		else:
			damage = _turn_(enemy, player_stats, dice_number, player=player_stats, enemy=enemy)
			message = get_message(damage, enemy, player_stats)
			if damage > 0:
				player_stats['Hp'] -= damage
		send_message(message, player_stats, enemy)
		turn += 1
	if player_stats['Hp'] < 0:
		send_message(f'{player_name} Died!', player=player_stats, enemy=enemy)
	else:
		send_message(f'{enemy_name} Died!', player=player_stats, enemy=enemy)
	return player_stats


fight({'Name': 'Warrior', 'Hp': 20, 'Attack': 15, 'Defense': 15, 'Agility': 5, 'Level': 1},{'Name': 'Orc', 'Hp': 20, 'Attack': 6, 'Defense': 10, 'Agility': 5, 'Level': 1})