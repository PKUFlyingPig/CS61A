from classes import *
from cards import *

try:
    import readline
except ImportError:
    pass

###########
# Parsing #
###########

def card_parse(line, handsize):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    elif len(tokens) > 1:
        raise SyntaxError('Too many inputs')
    card_index = tokens.pop(0)
    if not card_index.isdigit():
        raise SyntaxError('Wrong type of input')
    card_index = int(card_index)
    if card_index >= handsize or card_index < 0:
        raise SyntaxError('Invalid card number')
    return card_index

def name_parse(line):
    if not line:
        raise SyntaxError('No command given')
    return line

########
# REPL #
########

def read_eval_print_loop():
	while True:
		try:
			line = input('What is your name?> ')
			name = name_parse(line)
			break
		except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
			print('\nSee you next game!')
			return
		except SyntaxError as e:
			print('ERROR:', e)
	p1 = Player(player_deck, name)
	p2 = Player(opponent_deck, 'Opponent')
	print(WELCOME_MESSAGE)
	duel = Game(p1, p2)
	draw = True
	while True:
		if duel.game_won() == 1:
			print(WIN_MESSAGE)
			return
		elif duel.game_won() == 2:
			print(LOSE_MESSAGE)
			return
		print()
		try:
			if draw:
				p1.draw()
				p2.draw()
			else:
				draw = True
			p1.display_hand()
			print('Please enter the number next to the card you would like to play this round.')
			line = input('card> ')
			card_index = card_parse(line, len(p1.hand))
			duel.play_round(p1.play(card_index), p2.play_random())
			duel.display_scores()
		except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
			print('\nGood game. Bye!')
			return
		except AssertionError: # Deck out
			if p1.deck.is_empty() and p2.deck.is_empty():
				print(TIE_MESSAGE)
				return
			elif p1.deck.is_empty():
				print(PLAYER_DECKOUT_MESSAGE)
				return
			else:
				print(OPPONENT_DECKOUT_MESSAGE)
				return
		except SyntaxError as e:
			print('ERROR:', e)
			draw = False

#################
# Configuration #
#################

WELCOME_MESSAGE = """
Welcome to Magic: The Lambda-ing!

Your code has taken on a mind of its own and has
challenged you to a game of cards! If you need a refresher
on the rules, check out the section on the lab page.

Let's get this duel started, shall we?
"""

WIN_MESSAGE = """
You have vanquished your foe in a duel!

Congratulations! You won this game of Magic: The Lambda-ing!
"""

LOSE_MESSAGE = """
You have been defeated by your foe in a duel!

I'm sorry, you lost this game of Magic: The Lambda-ing.
"""

TIE_MESSAGE = """
You and your opponent have no cards left in your decks!

You tied this game of Magic: The Lambda-ing. Who will win if you play again?
"""

PLAYER_DECKOUT_MESSAGE = """
You have no cards left in your deck!

I'm sorry, you lost this game of Magic: The Lambda-ing.
"""

OPPONENT_DECKOUT_MESSAGE = """
Your opponent has no cards left in their deck!

Congratulations! You won this game of Magic: The Lambda-ing!
"""

if __name__ == '__main__':
    read_eval_print_loop()

