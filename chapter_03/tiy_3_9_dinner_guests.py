# --------------------------------------------------------------------------- #
# D. Rodriguez, 2019-11-24
# --------------------------------------------------------------------------- #
guests = ['phoebe bridgers', 'manu ginobili', 'kobe bryant', 'neil degrasse tyson']

print('Hey pals, I can only invite two people for dinner!')

# for name in guests:
#     print(f'{name.title()}, would you like to join me for dinner?')

guests.insert(0, 'adam jones')
guests.insert(len(guests)//2, 'john legend')
guests.append('Michael B. Jordan')

print(f"I'm inviting {len(guests)} guests for dinner.")

while len(guests) > 2:
    print(f"{guests.pop().title()}, I'm sorry to inform you that you are no longer invited to dinner")
    print(f"I'm inviting {len(guests)} guests for dinner.")


print(f"I'm inviting {len(guests)} guests for dinner.")

for name in guests:
    print(f'{name.title()}, would you like to join me for dinner?')


del guests[0:]

print(guests)