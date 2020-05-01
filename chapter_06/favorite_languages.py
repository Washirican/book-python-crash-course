# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     'albert': 'javascript'
#     }

# for name in favorite_languages.keys():
    # print(f'{name.title()}, thank you for taking the poll!')

# print()

# for name, language in favorite_languages.items():
    # print(f'{name.title()}\'s favorite langiage is {language.title()}.')

# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(f'Hi {name.title()}!')

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f'\t{name.title()}, I see you love {language}!')

# if 'erin' not in favorite_languages.keys():
#     print(f'\nErin, please take our poll!')

# for name in sorted(favorite_languages.keys()):
#     print(f'{name.title()}, thank you for taking the poll!')
#
# print(f'The following languages have been mentioned in the poll:')
# count = 0
# for language in set(favorite_languages.values()):
#     count += 1
#     print(f'{count}. {language.title()}')


favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_language.items():
    print(f'{name.title()}\'s favorite languages are:')
    for language in languages:
        print('\t' + language.title())
    print()
