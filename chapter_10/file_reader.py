# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())

filename = 'pi_digits.txt'

# Reading the whole file
# with open(filename) as file_object:
#     contents = file_object.read()
#
# print(contents.rstrip())
# print('-----------------')

# Reading one line at a time
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Reading whole file into a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
