# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-10-27, File Created.
# --------------------------------------------------------------------------- #
import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'mapping_global_data_sets/data/modis_2019_United_States.csv'
latitudes, longitudes, brightnesses = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        latitudes.append(float(row[0]))
        longitudes.append(float(row[1]))
        brightnesses.append(float(row[2]))

data = [
    {
        'type': 'scattergeo',
        'lon': longitudes,
        'lat': latitudes,
        'marker': {
            'size': [brightness/100 for brightness in brightnesses],
            'color': brightnesses,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'},
            }
        }
    ]

my_layout = Layout(title='Wildfires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='us_wildfires.html')
