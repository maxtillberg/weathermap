import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

########### Get Data
df = pd.read_csv('weather2.csv')

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server
#Konvertera från text till float
df['Dry bulb min winter'] = df['Dry bulb min winter'].astype(float)

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="Dry bulb min winter", size="Time zone",
                  color_continuous_scale=px.colors.diverging.Portland, hover_name="Name", size_max=9, zoom=3,
                  mapbox_style="carto-positron", height= 750)

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
