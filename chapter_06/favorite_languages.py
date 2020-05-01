favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'albert': 'javascript'
    }

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

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll!')