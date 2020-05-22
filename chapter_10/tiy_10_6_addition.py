# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-21
# --------------------------------------------------------------------------- #

print('\nEnter two numbers and I\'ll add them.')

first_number = input('First number: ')
second_number = input('Second number: ')


try:
    result = int(first_number) + int(second_number)
except ValueError:
    print('\nPlease, enter a number!')
else:
    print(f'\nThe sum of {first_number} and {second_number} is {result}.')

