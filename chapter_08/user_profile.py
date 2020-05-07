# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)


def build_profile(first_name, last_name, **user_info):
    """Function accepts an arbitrary number if keyword arguments"""
    print(type(user_info))
    print(user_info)

    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
