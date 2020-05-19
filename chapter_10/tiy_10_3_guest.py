# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-18
# --------------------------------------------------------------------------- #

filename = 'guest.txt'

guest_name = input('Please, enter your name: ')

with open(filename, 'w') as file_object:
    file_object.write(guest_name)
