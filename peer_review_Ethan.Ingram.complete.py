# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Ethan Ingram>
# Creation Date: <9/26/2020>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.
# You need to identify the issues and correct them)  #moved 2nd sentance to line 6

#  Reviewed by Ethan Ingram 9/26/2020

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	#   print() remove unnecessary function

def chooseCave():
		# issue: changed spaces to tab
		cave = ''
		while cave != '1' and cave != '2':
			print('Which cave will you go into? (1 or 2)')
			cave = input()
		# issue: caves instead of cave
		return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#   #sleep for 2 seconds incorrect comment
	#sleep for 3 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	#    print() remove unnecessary functions
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#   print 'Gobbles you down in one bite!' # () not included in statement
		print('Gobbles you down in one bite!')

playAgain = 'yes'
#   while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	#   caveNumber = choosecave()     #  lack of camel casing
	caveNumber = chooseCave()
	checkCave(caveNumber)
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		#   print("Thanks for planing") correction to playing
		print("Thanks for playing")
