from random import randint, choice
from os import system
from time import sleep

lore = 'It was start as an ordinary morning. You get up, drink your coffee, brush your teeth than grab your laptop and burst out the door. You don`t want to be late, especially because it was your PA day. You walkin down the street when suddenly you hear a strange voice from behind. You turn around and jump back. It was a big bad goofy clown. It open his mouth and makes that strange sound again. You want to run, but you are paralyzed. He pull out some strange pill, open your mouth, and force that pill down your throat. Before you can do anything you feel dizzy. Picture start flashing about a dark and cold cave, then you passed out.'
lorem = 'sed cras ornare arcu dui vivamus arcu felis bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque dignissim enim sit amet venenatis urna cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu non odio euismod lacinia at quis risus sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliq'
wake = 'Wake up! Wake Up! WAKE UP!!!'
short_lorem = 'tempor commodo ullamcorper a lacus vestibulum sed arcu non odio euismod lacinia at quis risus sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec'
in_cave = 'You open your eyes, but your vision is blurry for seconds. Your eyes are hurting, your ear is whistling. As your eyes are getting better you see a table. On the table there are 3 bag, each filled with some useful item.'
turn_around = 'When you turn around you see a little fluffy cat like creature walk through the only door of the room.'
creature = 'Finally awake! It`s 8:50, the attendance start in any minute and it`s your PA day you must slay the dragon! All you need is to get through some dark and cold room filled with mosnters and dead bodies of the ones who couldn`t escape. Good Luck!'



def get_class(klass):
	if klass == '0':
		return {'Name': 'Warrior', 'Hp': 20, 'Attack': 10, 'Defense': 15, 'Agility': 5, 'Level': 1}
	elif klass == '1':
		return {'Name': 'Mage', 'Hp': 15, 'Attack': 15, 'Defense': 5, 'Agility': 10, 'Level': 1}
	elif klass == '2':
		return {'Name': 'Thief', 'Hp': 10, 'Attack': 15, 'Defense': 5, 'Agility': 20, 'Level': 1}


def change_text(text):
	print(text)
	chars = sum([[chr(x) for x in range(97, 123)], [' ' for _ in range(15)]], [])
	change = 25
	while change != 0:
		i = randint(0, len(text)-1)
		text = text.replace(text[i], choice(chars))
		system('clear')
		print(text)
		sleep(0.1)
		change -= 1
	system('clear')

def choose_class():
	bags = [('sword', 'shield'),('bow', 'arrows') , ('staff', 'potions')]
	print('Which one do you want to take with you?\n The one with the:')
	sleep(1)
	for i, bag in enumerate(bags):
		print(f'{i} {bag[0]} and {bag[1]}')
	sleep(1)
	choice = input('You choose: ')
	system('clear')
	return get_class(choice)

def start_lore():
	system('clear')
	print(lorem)
	sleep(2)
	change_text(lorem)
	input(lore)
	system('clear')
	input(wake)
	system('clear')
	print(short_lorem)
	sleep(2)
	change_text(short_lorem)
	print(in_cave)
	player_class = choose_class()
	input(turn_around)
	input(creature)
	return player_class