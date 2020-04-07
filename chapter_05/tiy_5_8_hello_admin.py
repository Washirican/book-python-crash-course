# --------------------------------------------------------------------------- #
# Script Title: 
# Change Log: (Who, When, What)
# D. Rodriguez, 2020-01-29, Initial release
# --------------------------------------------------------------------------- #
usernames = ['Dan DaMan', 'Flaco McFlaco', 'El Macaracachimba', 'admin', 'Michael B. Jordan']

for name in usernames:
    if name == 'admin':
        print('Hello {}, would you like to print a Status Report?'.format(name))
    else:
        print('Hello {}, thank you for logging in again!'.format(name))
