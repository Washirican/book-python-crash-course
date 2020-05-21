# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-18
# --------------------------------------------------------------------------- #

filename = 'programming_poll.txt'

active = True

while active:
    poll_response = input('What do you like about Python programming? '
                          '(Type \'q\' to quit): ')
    if poll_response == 'q':
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f'{poll_response}\n')

