# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-09-13, File created.
# --------------------------------------------------------------------------- #
import csv
from datetime import datetime
from matplotlib import pyplot as plt


def get_weather_data(filename):
    """Get weather data from file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high and low temperatures.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


# Get Sitka weather data.
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = get_weather_data(filename)

# Create plot.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Add Sitka weather data to plot
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Get Death Valley data.
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = get_weather_data(filename)

# Add Death Valley date to plot.
ax.plot(dates, highs, c='green', alpha=0.5)
ax.plot(dates, lows, c='magenta', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures - 2018"
title += "\nSitka, AK and Death Valley, CA"

plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()

