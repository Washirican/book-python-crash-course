# NOTE (D. Rodriguez 2020-05-21): Original code
# import json
#
# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# NOTE (D. Rodriguez 2020-05-21): My code
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

