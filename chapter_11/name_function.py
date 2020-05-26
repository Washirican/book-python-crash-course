
# NOTE (D. Rodriguez 2020-05-25): Original code
# def get_formatted_name(first, last, middle=''):
#     """Generate a neatly formatted full name."""
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()


# NOTE (D. Rodriguez 2020-05-25): My code
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

