# NOTE (D. Rodriguez 2020-05-21): Original code
import json

# def get_stored_username():
#     """Get stored username if available."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def get_new_username():
#     """Prompt for a new username."""
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username
#
# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = get_new_username()
#         print(f"We'll remember you when you come back, {username}!")
#
# greet_user()

# NOTE (D. Rodriguez 2020-05-21): My code

# username = input('What is your name? ')
#
# filename = 'username.json'
#
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f'We\'ll remember you when you come back,  {username}!')

# NOTE (D. Rodriguez 2020-05-23): Combine 2 programs into one file (pg. 205)

# Load username if it has already been loaded
# Otherwise, prompt for the username and store it

# filename = 'username.json'
#
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("Whats your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you next time {username}!")
# else:
#     print(f"Welcome back, {username}!")


# NOTE (D. Rodriguez 2020-05-23): Refactor code (pg. 206)
# def greet_user():
#     """Greet user by name."""
#     filename = 'username.json'
#
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you next time, {username}!")
#     else:
#         print(f"Welcome back, {username}!")
#
#
# greet_user()

# NOTE (D. Rodriguez 2020-05-23): New function to get stored username

# def get_stored_username():
#     """Get stored username if available."""
#     filename = 'username.json'
#
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
#
# def greet_user():
#     """Greet user by name."""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'
#
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you next time, {username}!")
#
#
# greet_user()

# NOTE (D. Rodriguez 2020-05-23): Move code that prompts for a new username
#  to new function

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What's your name? ")
    filename = 'username.json'

    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you next time, {username}!")


greet_user()

