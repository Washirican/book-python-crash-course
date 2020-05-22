# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-21
# --------------------------------------------------------------------------- #

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass
    else:
        print(f'\nReading file: {filename}')
        print(contents)
