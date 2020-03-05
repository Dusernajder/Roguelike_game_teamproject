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


def _turn_(attacker, defender):
	attack = throw_six_sided_dice(2)
	defense = throw_six_sided_dice(2)
	mssg = 'None'
	return calculate_damage(attacker['Attack']+attack, defender['Defense']+defense, defender['Agility'])


def get_message(damage, attacker, defender):
	if damage <= 0:
		name = defender['Name']
		return f'{name} dodged the attack!'
	else:
		name = attacker['Name']
		return f'{name} caused {damage} point(s) of damage!'
		


def fight(player_stats, enemy):
	util.clear_screen()
	printing.print_fight_board(player_stats, enemy)
	message = None
	turn = 1
	while not_dead(player_stats, enemy):
		attack = throw_six_sided_dice(2)
		defense = throw_six_sided_dice(2)
		if turn % 2 != 0:
			damage = _turn_(player_stats, enemy)
			message = get_message(damage, player_stats, enemy)
			if damage > 0:
				enemy['Hp'] -= damage
		else:
			damage = _turn_(enemy, player_stats)
			message = get_message(damage, enemy, player_stats)
			if damage > 0:
				player_stats['Hp'] -= damage
		util.clear_screen()
		printing.print_fight_board(player_stats, enemy, mssg=message)
		turn += 1
	return player_stats

