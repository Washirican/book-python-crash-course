# --------------------------------------------------------------------------- #
# D. Rodriguez, 2019-12-01
# --------------------------------------------------------------------------- #
pizzas = ['hawaiian', 'pepperoni', 'Margherita']
friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('bacon')

for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print()
for pizza in friend_pizzas:
    print(f'My friend likes {pizza.title()} pizza.')

print('\nWe really love pizza!')