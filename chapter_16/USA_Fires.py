# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-11-02, File Created.
# Refactor code fallowing Plotly documentation examples from:
# https://plotly.com/python/bubble-maps/#united-states-bubble-map
# --------------------------------------------------------------------------- #
from datetime import datetime
import csv
import plotly.graph_objs as go
from plotly import offline

filename = 'mapping_global_data_sets/data/modis_2019_United_States.csv'
latitudes, longitudes = [], []
brightnesses, dates = [], []
hover_texts = []

num_rows = 10_000

# Read data from csv file and save it to relevant lists
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get latitudes, longitudes, brightness and dates.
    row_num = 0
    for row in reader:
        dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
        brightnesses.append(float(row[2]))
        hover_texts.append(
                f"{datetime.strptime(row[5], '%Y-%m-%d').strftime('%m/%d/%y')}"
                f" - {float(row[2])}")

        latitudes.append(float(row[0]))
        longitudes.append(float(row[1]))

        row_num += 1
        if row_num == num_rows:
            break

# This should not be public!
mapbox_access_token = 'pk.eyJ1Ijoid2FzaGlyaWNhbiIsImEiOiJja2gyeG9kdWUxYXJoMnJybmlweXg2aTRiIn0.AnaSkQ6ZFXEHsd4kWYoQxw'  # open(".mapbox_token").read()

# Define chart in a way that is better to customize it.
fig = go.Figure(go.Scattermapbox(
        lon=longitudes,
        lat=latitudes,
        text=hover_texts,
        marker=go.scattermapbox.Marker(
                {
                    'size': [brightness / 20 for brightness in brightnesses],
                    'color': brightnesses,
                    # 'line_color': 'rgb(40,40,40)',
                    'colorscale': 'YlOrRd',
                    'colorbar': {'title': 'Brightness'},
                    }
                ),

        ))

fig.update_layout(
        title_text='United States Wildfires',
        hovermode='closest',
        mapbox_style='carto-positron',
        mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=go.layout.mapbox.Center(
                        lat=38,
                        lon=-94,
                        ),
                pitch=0,
                zoom=3.5,
                )
        )

offline.plot(fig, filename='us_wildfires.html')
