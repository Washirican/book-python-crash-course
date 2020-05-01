# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#         },
#
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         },
#
#     }
#
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

users = {
    'aeinstein': {
        'first_name': 'albert',
        'last_name': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first_name': 'marie',
        'last_name': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
