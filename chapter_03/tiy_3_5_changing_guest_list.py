# --------------------------------------------------------------------------- #
# Script Title: 
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-11-03, Initial release
# --------------------------------------------------------------------------- #

guests = ['phoebe bridgers', 'manu ginobili', 'kobe bryant', 'neil degrasse tyson']

for name in guests:
    print(f'{name.title()}, would you like to join me for dinner?')

cantmakeit = 'kobe bryant'

print(f"\n{cantmakeit.title()}, won't be able to join uus for dinner tonight.\n")

newguest = 'Jimmy page'

guests.append(newguest)
guests.remove(cantmakeit)

for name in guests:
    print(f'{name.title()}, would you like to join me for dinner?')
