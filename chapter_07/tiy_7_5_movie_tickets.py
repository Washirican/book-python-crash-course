# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-02
# --------------------------------------------------------------------------- #


age = ''

while age != 'done':
    prompt = '\nWhat is your age? (Enter \'done\' when done)'
    age = input(prompt)

    if age == 'done':
        break
    elif int(age) <= 3:
        print(f'Your ticket is free!')
    elif 3 < int(age) <= 12:
        print('Your ticket is $10')
    elif int(age) > 12:
        print('Your ticket is $15')
