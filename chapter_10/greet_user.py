# NOTE (D. Rodriguez 2020-05-21): Original code
# import json
#
# filename = 'username.json'
#
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back, {username}!")

import json

# NOTE (D. Rodriguez 2020-05-21): My code


filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f'Welcome back, {username}!')
