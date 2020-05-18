# filename = 'pi_million_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(f'{pi_string[:52]}')
print('{:,}'.format(len(pi_string)))

birthday = '021980'

if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi!')
