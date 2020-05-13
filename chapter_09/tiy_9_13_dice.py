# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
# --------------------------------------------------------------------------- #

from random import randint


class Die:
    """Die class"""

    def __init__(self, sides=6):
        """Constructor for Die"""
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)


die_6 = Die()
die_10 = Die(10)
die_20 = Die(20)

die_list = [die_6, die_10, die_20]

for die in die_list:
    print(f'\nRolling {die.sides}-sided die...')
    for times in range(10):
        print(f'Roll #{times + 1}:')
        die.roll_die()

