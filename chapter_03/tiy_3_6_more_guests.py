# --------------------------------------------------------------------------- #
# D. Rodriguez, 2019-11-24
# --------------------------------------------------------------------------- #

guests = ['phoebe bridgers', 'manu ginobili', 'kobe bryant', 'neil degrasse tyson']

print('Hey pals, I just found a bigger table for dinner!')

# for name in guests:
#     print(f'{name.title()}, would you like to join me for dinner?')

guests.insert(0, 'adam jones')
guests.insert(len(guests)//2, 'john legend')
guests.append('Michael B. Jordan')


for name in guests:
    print(f'{name.title()}, would you like to join me for dinner?')
