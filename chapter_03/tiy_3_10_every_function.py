# --------------------------------------------------------------------------- #
# D. Rodriguez, 2019-11-24
# --------------------------------------------------------------------------- #
places = ['croatia', 'portugal', 'argentina', 'australia', '']

print('Hey pals, I can only invite two people for dinner!')

# for name in guests:
#     print(f'{name.title()}, would you like to join me for dinner?')

places.insert(0, 'adam jones')
places.insert(len(places)//2, 'john legend')
places.append('Michael B. Jordan')

print(places)
print(sorted(places))
print(places)

print(sorted(places, reverse=True))
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)


while len(places) > 2:
    print(f"{places.pop().title()}, I'm sorry to inform you that you are no longer invited to dinner")
    print(f"I'm inviting {len(places)} guests for dinner.")


print(f"I'm inviting {len(places)} guests for dinner.")

for name in places:
    print(f'{name.title()}, would you like to join me for dinner?')


del places[0:]

print(places)
