# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-17
# --------------------------------------------------------------------------- #
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read().replace('Python', 'C')

    print(contents)
