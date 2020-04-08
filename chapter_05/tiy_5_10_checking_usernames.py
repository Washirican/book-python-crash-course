# --------------------------------------------------------------------------- #
# Script Title: 
# Change Log: (Who, When, What)
# D. Rodriguez, 2020-01-29, Initial release
# --------------------------------------------------------------------------- #

current_users = ['washirican', 'Mastodonte', 'natifca', 'daniel_andres',
                 'flaco_mcflaco', 'jordan']
new_users = ['chilindrina', 'mastodonte', 'jirafales', 'florinda', 'chavo']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('Username {} is already in use. Please, select a new Username.'
              .format(new_user))
    else:
        print('Username {} is available!'.format(new_user))

