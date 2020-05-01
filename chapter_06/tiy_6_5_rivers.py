rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print()
print('River on this list:')
for river in rivers.keys():
    print(river)

print()
print('Countries on this list:')
for country in rivers.values():
    print(country.title())
