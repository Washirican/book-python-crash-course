# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-07
# --------------------------------------------------------------------------- #


def build_profile(first_name, last_name, **user_info):
    """Function accepts an arbitrary number if keyword arguments"""
    # print(type(user_info))
    # print(user_info)

    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info


user_profile = build_profile('daniel', 'rodriguez',
                             age=40,
                             employer='boeing',
                             location='kirkland',
                             field='aerospace')
print(user_profile)

