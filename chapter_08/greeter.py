# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def greet_user(username):
#     """Display a simple greeting"""
#     # 'username' is a PARAMETER the function needs to do it's job.
#     print(f'Hello, {username.title()}!')


# if __name__ == '__main__':
#     # 'daniel' is an ARGUMENT passed from a function call to a function
#     greet_user('sarah')

def get_formatted_name(first_name, last_name):
    """Return a full name, formatted"""
    full_name = f'{first_name.title()} {last_name.title()}'
    return full_name

while True:
    print('\nPlease, tell me your name.')
    print('(enter \'q\' at any time to quit)')
    
    f_name = input('First Name: ')
    if f_name == 'q':
        break

    l_name = input('Last Name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}!')
