'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    fig.add_trace(go.Choroplethmapbox(
        geojson=montreal_data,
        locations=locations,
        z=z_vals,
        colorscale=colorscale,
        showscale=False, 
        marker_line_color='white', 
        marker_line_width=0.5,  # Line width between neighborhoods
        hoverinfo='all',  
    ))
    return fig




def add_scatter_traces(fig, street_df):
    # Assuming 'type' column categorizes the paths and 'longitude' and 'latitude' columns exist
    for path_type, group in street_df.groupby('TYPE_AXE'):
        fig.add_trace(go.Scattermapbox(
            lon=group['longitude'],
            lat=group['latitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,  
                opacity=0.7
            ),
            name=path_type,
            hoverinfo='text',
            hovertext=group['NOM_PROJET']  # Assuming a column for the project name
        ))
    return fig


