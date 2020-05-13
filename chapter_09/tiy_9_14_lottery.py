# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
# --------------------------------------------------------------------------- #
from random import choice
import string

numbers = list(range(10))
letters = list(string.ascii_uppercase)

possibilities = numbers + letters

winning_ticket = ''
print("\nLet's see what the winning ticket is...")

while len(winning_ticket) < 4:
    pulled_item = str(choice(possibilities))

    if pulled_item not in winning_ticket:
        print(f'\tWe pulled a \'{pulled_item}\'...')
        winning_ticket += pulled_item


print(f'\nAnd the Lottery winner is {winning_ticket}!')
