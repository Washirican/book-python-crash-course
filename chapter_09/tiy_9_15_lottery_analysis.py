# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
# --------------------------------------------------------------------------- #

from random import choice
import string


def lottery(possibilities , characters):
    winning_ticket = ''
    while len(winning_ticket) < characters:
        pulled_item = str(choice(possibilities))

        if pulled_item not in winning_ticket:
            # print(f'\tWe pulled a \'{pulled_item}\'...')
            winning_ticket += pulled_item
    return winning_ticket


numbers = list(range(10))
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)

possibilities = numbers + uppercase_letters + lowercase_letters

my_ticket = lottery(possibilities, 4)
print("\nLet's see what the winning ticket is...")

times = 0

winning_ticket = ''
while my_ticket != winning_ticket:
    times += 1
    winning_ticket = lottery(possibilities, 4)

print(f'And the Lottery winner is \'{winning_ticket}\'!')
print()
print(f'My Lottery ticket number is \'{my_ticket}\'.')
print(f'It took {times:,} tries for me to win...')

