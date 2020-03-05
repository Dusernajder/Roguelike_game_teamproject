from random import randint
import printing


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
		


def figth(player_stats):
	enemy = {'Name': 'Orc', 'Hp': 15, 'Attack': 10, 'Defense': 10, 'Agility': 10, 'Level': 1}
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
		printing.print_fight_board(player_stats, enemy, mssg=message)
		turn += 1
	return player_stats






# def choose_class():
# 	for i, x in enumerate(['Warrior', 'Mage', 'Thief']):
# 		print(f'{i} {x}')
# 	choice = input('Choose class:')
# 	if choice == '0':
# 		return {'Name': 'Warrior', 'Hp': 20, 'Attack': 10, 'Defense': 15, 'Agility': 5, 'Level': 1}
# 	elif choice == '1':
# 		return {'Name': 'Mage', 'Hp': 15, 'Attack': 15, 'Defense': 5, 'Agility': 10, 'Level': 1}
# 	elif choice == '2':
# 		return {'Name': 'Thief', 'Hp': 10, 'Attack': 15, 'Defense': 5, 'Agility': 20, 'Level': 1}


# def main():
# 	player_class = choose_class()
# 	player_class = figth(player_class)
# 	if player_class['Hp'] <= 0:
# 		print('GameOver')
# 	else:
# 		print('Win')



# if __name__ == '__main__':
# 	main()


# printing.print_fight_board(attacker, defender, mssg=f'{name} Dodged!') 
# printing.print_fight_board(attacker, defender, mssg=f'{name} cause {damage} points of damage!')
# printing.print_fight_board(attacker, defender, mssg=f'{name} Blocked!')