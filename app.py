import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

########### Get Data
weatherdata = pd.read_csv('weather.csv', encoding = "cp1252")
df = pd.read_csv(url, encoding = "cp1252")
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="Dry bulb max summer", size="Time zone",
                  color_continuous_scale=px.colors.diverging.Portland, hover_name="Name", size_max=9, zoom=3,
                  mapbox_style="carto-positron")

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server

fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
