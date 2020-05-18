# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-17
# --------------------------------------------------------------------------- #

filename = 'learning_python.txt'

print('\nRead entire file at once...')
with open(filename) as file_object:
    content = file_object.read()

print(content)

print('\nLooping over the file object...')
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print('\nStoring lines on a list')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
