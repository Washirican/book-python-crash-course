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

fig = go.Figure()

fig.add_trace(go.Scattergeo(
        locationmode='USA-states',
        lon=longitudes,
        lat=latitudes,
        text=hover_texts,
        marker=dict(
                size=brightnesses,  # [brightness/10 for brightness in brightnesses],
                color=brightnesses,
                line_color='rgb(40,40,40)',
                colorscale='YlOrRd',
                line_width=0.5,
                sizemode='area',
                colorbar={'title': 'Brightness'},
                ),

        ))

fig.update_layout(
        title_text='United States Wildfires',
        # showlegend=True,
        geo=dict(
                scope='usa',
                landcolor='rgb(217, 217, 217)',
                )
        )

# fig.show()

offline.plot(fig, filename='us_wildfires.html')

