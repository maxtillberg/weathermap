import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

df = px.data.carshare()

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server

fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")

app.layout = html.Div(
    [
        html.H1("IDA ICE Weather files"),
        html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
