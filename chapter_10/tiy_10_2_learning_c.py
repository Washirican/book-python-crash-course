# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-17
# --------------------------------------------------------------------------- #
filename = 'learning_python.txt'

print('\nRead entire file...')
with open(filename) as file_object:
    print(file_object.read().replace('Python', 'C'))


print('\nRead one line at a time...')
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').strip())


print('\nRead entire file into a list...')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C').strip())
