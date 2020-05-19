# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-18
# --------------------------------------------------------------------------- #

filename = 'guest_book.txt'

active = True

with open(filename, 'a') as file_object:

    while active:
        guest_name = input('\nEnter your name (\'q\' to quit): ')
        if guest_name == 'q':
            active = False
        else:
            print(f'Welcome back, {guest_name}!')
            file_object.write(f'{guest_name}\n')
a
