# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-21
# --------------------------------------------------------------------------- #

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as book:
            contents = book.read()
    except FileNotFoundError:
        pass

    else:
        words = contents.lower().split()
        # words = contents.lower()

        common_word = 'the'
        common_word_count = words.count(common_word)
        print(f'\nThe word \'{common_word}\' appears about '
              f'{common_word_count} times in {filename}')
