# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-10-18, File Created.
# --------------------------------------------------------------------------- #

import csv
from datetime import datetime
from matplotlib import pyplot as plt


def get_weather_data(filename):
    """Get weather data from file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_index = header_row.index('DATE')
        station_name_index = header_row.index('NAME')
        highs_index = header_row.index('TMAX')
        lows_index = header_row.index('TMIN')

        # Get dates, high and low temperatures.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            # TODO (D. Rodriguez 2020-10-18): This reads station name from
            #  every row even when we know all rows have the same name. Need
            #  to revise it to read name only once.
            station_name = row[station_name_index]

            try:
                high = int(row[highs_index])
                low = int(row[lows_index])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return station_name, dates, highs, lows


# Get weather data.
filename = 'data/sitka_weather_2018_full.csv'
# filename = 'data/death_valley_2018_full.csv'

name, dates, highs, lows = get_weather_data(filename)

# Create plot.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Add Sitka weather data to plot
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f'Daily High and Low Temperatures - 2018' \
        f'\n{name}'

plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()

