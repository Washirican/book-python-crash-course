# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-01
# --------------------------------------------------------------------------- #
player_0 = {
    'first_name': 'michael',
    'last_name': 'jordan',
    'jersey_number': 23,
    'team': 'bulls',
    }

player_1 = {
    'first_name': 'larry',
    'last_name': 'bird',
    'jersey_number': 33,
    'team': 'celtics',
    }

player_2 = {
    'first_name': 'magic',
    'last_name': 'johnson',
    'jersey_number': 32,
    'team': 'bulls',
    }

players = [player_0, player_1, player_2]

for player in players:
    print(f"{player['first_name'].title()} {player['last_name'].title()} "
          f"wears number {player['jersey_number']} and plays for the "
          f"{player['team'].title()}.")

