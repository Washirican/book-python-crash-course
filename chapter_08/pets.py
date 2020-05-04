# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet(pet_name='willie')


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f'\nI have a {animal_type}.')
    print(f'My {animal_type}\'s name is {pet_name.title()}.')


if __name__ == '__main__':
    describe_pet(pet_name='lola')
    describe_pet(pet_name='simba', animal_type='cat')


