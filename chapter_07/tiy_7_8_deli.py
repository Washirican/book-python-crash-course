# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #

sandwich_orders = ['blt', 'cubano', 'grilled cheese', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'\nI made your {current_sandwich.title()} sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\nAll sandwich orders have been fulfilled! We\'ve made the following:')

for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()} sandwich.')

