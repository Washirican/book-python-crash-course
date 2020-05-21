# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-18
# --------------------------------------------------------------------------- #

filename = 'guest_book.txt'

active = True

while active:
    guest_name = input('\nEnter your name (\'q\' to quit): ')
    if guest_name == 'q':
        active = False
    else:
        with open(filename, 'a') as file_object:
            print(f'Welcome back, {guest_name}!')
            file_object.write(f'{guest_name}\n')
