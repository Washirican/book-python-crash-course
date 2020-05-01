favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'albert': 'javascript'
    }

names = ['jen', 'daniel', 'natalia', 'sarah', 'yolanda', 'alma', 'phil']

for name in names:
    if name in favorite_languages.keys():
        print(f'{name.title()}, thank you for taking the poll!')
        print(f'\tYour favorite language is {favorite_languages[name]}.')
    else:
        print(f'{name.title()}, please take the poll!')
