import json
import requests

request_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson'

response = requests.get(request_url)

new_data = response.json()

# Explore the structure of the data.
# filename = 'data/my_eq_data_1_day_m1.json'
#
# with open(filename, 'w') as f:
#     json.dump(new_data, f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(new_data, f, indent=4)
