# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


def make_pizza(*toppings):
    """Print list of toppings that have been requested."""
    print(f'\nMaking a pizza with the following toppings:')

    for topping in toppings:
        print(f'\t{topping.title()}')


make_pizza('pepperoni', 'olives', 'arugula', 'extra cheese')
