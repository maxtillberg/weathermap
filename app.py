import plotly.graph_objects as go # or plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

mapbox_access_token = open(".mapbox_token").read()

fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server

#app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

#app.run_server(debug=True, use_reloader=False) 
if __name__ == "__main__":
    app.run_server(debug=True)
