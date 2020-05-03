# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #

sandwich_orders = ['pastrami', 'blt', 'cubano', 'pastrami', 'grilled cheese',
                   'pastrami']

finished_sandwiches = []

print('\nSorry, we ran out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'\nI made your {current_sandwich.title()} sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\nAll sandwich orders have been fulfilled! We\'ve made the following:')

for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()} sandwich.')





