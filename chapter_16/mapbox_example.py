# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-11-03, File created.
# --------------------------------------------------------------------------- #
import plotly.graph_objects as go

mapbox_access_token = 'pk.eyJ1Ijoid2FzaGlyaWNhbiIsImEiOiJja2gyeG9kdWUxYXJoMnJybmlweXg2aTRiIn0.AnaSkQ6ZFXEHsd4kWYoQxw'  #open(".mapbox_token").read()

fig = go.Figure(go.Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=go.scattermapbox.Marker(
                size=14
                ),
        text=['Montreal'],
        ))

fig.update_layout(
        hovermode='closest',
        mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=go.layout.mapbox.Center(
                        lat=45,
                        lon=-73
                        ),
                pitch=0,
                zoom=5
                )
        )

fig.show()
