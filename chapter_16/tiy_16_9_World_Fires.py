# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-10-27, File Created.
# --------------------------------------------------------------------------- #
import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'mapping_global_data_sets/data/modis_2019_United_States.csv'
latitudes, longitudes = [], []
brightnesses, dates = [], []
hover_texts = []

num_rows = 10_000

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get latitudes, longitudes, brightness and dates.
    row_num = 0
    for row in reader:
        dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
        brightnesses.append(float(row[2]))
        hover_texts.append(
                f"{datetime.strptime(row[5], '%Y-%m-%d').strftime('%m/%d/%y')} "
                f"- {float(row[2])}")

        latitudes.append(float(row[0]))
        longitudes.append(float(row[1]))

        row_num += 1
        if row_num == num_rows:
            break

data = [
    {
        'type': 'scattergeo',
        'lon': longitudes,
        'lat': latitudes,
        'text': hover_texts,
        'marker': {
            'size': [brightness/20 for brightness in brightnesses],
            'color': brightnesses,
            'colorscale': 'YlOrRd',
            # 'reversescale': True,
            'colorbar': {'title': 'Brightness'},
            }
        }
    ]

my_layout = Layout(title='United States Wildfires')
my_layout.geo.update(
        showcountries=True,
        fitbounds='locations',
        )

fig = {
    'data': data,
    'layout': my_layout,
    }

offline.plot(fig, filename='us_wildfires.html')
