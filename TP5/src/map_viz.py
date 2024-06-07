'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    fig.add_trace(go.Choropleth(
        geojson=montreal_data,
        locations=locations,
        z=z_vals,
        colorscale=colorscale,
        showscale=False,  # Hide the color scale bar
        marker_line_color='white',  # Line color between neighborhoods
        marker_line_width=0.5,  # Line width between neighborhoods
    ))
    fig.update_geos(fitbounds="locations")  # Fit the bounds to the geojson locations
    return fig



def add_scatter_traces(fig, street_df):
    # Assuming 'type' column categorizes the paths and 'longitude' and 'latitude' columns exist
    for path_type, group in street_df.groupby('TYPE_AXE'):
        fig.add_trace(go.Scattermapbox(
            lon=group['longitude'],
            lat=group['latitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=20,
                opacity=0.7
            ),
            name=path_type,
            hoverinfo='text',
        ))
    fig.update_layout(mapbox_style="light", mapbox_zoom=10, mapbox_center={"lat": 45.5017, "lon": -73.5673})
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

