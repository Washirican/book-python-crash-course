# NOTE (D. Rodriguez 2020-05-21): Original code
# import json
#
# filename = 'numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)
#
# print(numbers)

# NOTE (D. Rodriguez 2020-05-21): My code

import json

filename = 'numbers.json'

with open(filename, 'r') as f:
    numbers = json.load(f)

print(numbers)
