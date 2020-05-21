# ---- Original Code ----
# def count_words(filename):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
#
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)


# NOTE (D. Rodriguez 2020-05-21): My Code
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Sorry, file {filename} was not found.')
    else:
        words = contents.split()
        num_words = len(words)
        return num_words

# ---- Using a single file ----
# filename = 'alice.txt'
# num_words = count_words(filename)
# print(f'The file {filename} has about {num_words} words.')


# NOTE (D. Rodriguez 2020-05-21):  Using multiple files
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    num_words = count_words(filename)
    print(f'The file {filename} has about {num_words} words.')
