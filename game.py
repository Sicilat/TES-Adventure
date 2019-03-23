###################
#  TES-Adventure  #
# Made by Sicilat #
###################

import os, sys, cmd, textwrap, time, random

class Player():
	def __init__(self):
		self.mana = 0

def clear():
	os.system('clear||cls')

def setup_game():
	

def show_help_menu():
	clear()
	print('This is the help menu !')
	print('All this current page can be found into the official documentation !')

def load_game():
	print('WIP')

def handle_main_menu_display():
	clear()
	print('###################')
	print('#  TES-Adventure  #')
	print('# Made by Sicilat #')
	print('###################')
	print('       -Play-      ')
	print('       -Load-      ')
	print('       -Help-      ')
	print('       -Quit-      ')
	handle_main_menu_options()

def handle_main_menu_options():
	asw = input('> ')
	while asw.lower() not in ['play', 'load', 'help', 'quit', 'start', 'exit', 'about']:
		print('Please enter a supported answer !')
		asw = input('> ')
	if asw.lower() == 'play' or asw.lower() == 'start':
		setup_game()
	elif asw.lower() == 'load':
		load_game()
	elif asw.lower() == 'help' or asw.lower() == 'about':
		show_help_menu()
	else:
		clear()
		print('Thank you for playing !')
		sys.exit()

print("Here's the main program !")
handle_main_menu_display()