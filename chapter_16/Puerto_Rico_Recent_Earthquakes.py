# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-10-27, File Created.
# Plot recent earthquake activity in Puerto Rico
# --------------------------------------------------------------------------- #

import requests
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Extra credit: Get recent earthquake data from USGS.
request_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/' \
              '1.0_day.geojson'

response = requests.get(request_url)
recent_eq_data = response.json()

# Get chart title from json data
title = recent_eq_data['metadata']['title']

# Extract earthquake dictionaries from json data
all_eq_dicts = recent_eq_data['features']
# print(len(all_eq_dicts))

# Get earthquake magnitudes and store them in a list.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:

    # Filter for Puerto Rico in earthquake title
    if 'Puerto Rico' in eq_dict['properties']['title']:

        # Refactor to use values directly and not saving to temporary variables
        mags.append(eq_dict['properties']['mag'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])

# Define chart in a way that is better to customize it.
data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        # 'locationmode': 'USA-states',
        'marker': {
            # Define marker size depending on earthquake magnitude.
            'size': [5*mag for mag in mags],

            # Customizing marker colors.
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
            }
        }
    ]

my_layout = Layout(title=title)
my_layout.geo.update(
        showcountries=True,
        fitbounds='locations',
        # scope='usa',
        # scope='south america',
        landcolor='rgb(217, 217, 217)',
        )

fig = {
    'data': data,
    'layout': my_layout
    }

offline.plot(fig, filename='puerto_rico_earthquakes.html')
