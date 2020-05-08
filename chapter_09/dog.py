# class Dog:
#     """A simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")
#
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)
#
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
#
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()


class Dog:
    """A simple dog class."""

    # Define init method with 3 parameters
    def __init__(self, name, age):
        """Constructor for Dog"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f'\n{self.name} is now sitting!')

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f'\n{self.name} rolled over!')


my_dog = Dog('lola', 8)

print(f'\nMy dog\'s name is {my_dog.name}')
print(f'\nMy dog is {my_dog.age} years old.')

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Jack', 13)

print(f'\nMy dog\'s name is {your_dog.name}')
print(f'\nMy dog is {your_dog.age} years old.')

your_dog.sit()
your_dog.roll_over()
