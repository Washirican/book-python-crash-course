# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first_name': first_name, 'last_name': last_name}

    if age:
        person['age'] = age

    return person


if __name__ == "__main__":
    person = build_person('daniel', 'rodriguez')
    print(person)
