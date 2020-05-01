#  # Store information about a pizza being ordered.
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
#
# # Summarize the order.
# print(f"You ordered a {pizza['crust']}-crust pizza "
#     "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print("\t" + topping)


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza with the following "
      f"toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)