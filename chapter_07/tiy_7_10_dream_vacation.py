# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #

dream_vacation = {}

active_poll = True

while active_poll:
    name = input('\nWhat is your name? ')
    response = input('What is your dream vacation spot? ')

    dream_vacation[name] = response

    repeat = input('\nWould you like to let another person answer the poll? '
                   '(\'yes\' or \'no\') ')

    if repeat == 'no':
        active_poll = False

print('\nPoll Results:')
for name, vacation_spot in dream_vacation.items():
    print(f'\t{name.title()} would like to vacation in'
          f' {vacation_spot.title()}.')
