# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-09-13, File created.
# --------------------------------------------------------------------------- #
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_full.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and precipitation from file.
    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            current_precipitation = float(row[3])
        except ValueError:
            print(f'Missing date for {current_date}')
        else:
            dates.append(current_date)
            precipitation.append(current_precipitation)

# Plot precipitation.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitation, c='red')

# Format plot.
plt.title('Daily Precipitation - 2018', fontsize=24)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.ylabel('Precipitation', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

