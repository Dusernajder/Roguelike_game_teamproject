from random import randint


def roll_two_D6(): #2 pieces of SixSidedDice
	return randint(1, 6) + randint(1, 6)


def calculate_damage(attack, defense, agility):
	if agility >= randint(1,100): #calculate dodge chance
		return 0
	return attack - defense


def clash(attacker, defender):
	attack = roll_two_D6()
	name = attacker['Name']
	input(f'{name} rolled {attack}')
	defense = roll_two_D6()
	name = defender['Name']
	input(f'{name} rolled {defense}')
	if attack > defense:
		damage = calculate_damage(attacker['Attack']+attack, defender['Defense']+defense, defender['Agility'])
		if damage <= 0:
			name = defender['Name']
			input(f'{name} Dodged!') 
		else:
			name = attacker['Name']
			input(f'{name} cause {damage} points of damage!')
			defender['Hp'] -= damage
	return attacker, defender


def not_dead(player, enemy):
	if player['Hp'] > 0 and enemy['Hp'] > 0:
		return True
	return False


def fight(player_class):
	enemy = {'Name': 'Orc', 'Hp': 15, 'Attack': 10, 'Defense': 10, 'Agility': 10}
	while True:
		player_class, enemy = clash(player_class, enemy)
		if not_dead(player_class, enemy) == False:
			break
		enemy, player_class = clash(enemy, player_class)
		if not_dead(player_class, enemy) == False:
			break
	return player_class
		


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


def main():
	player_class = choose_class()
	player_class = fight(player_class)
	if player_class['Hp'] <= 0:
		print('GameOver')
	else:
		print('Win')



if __name__ == '__main__':
	main()
