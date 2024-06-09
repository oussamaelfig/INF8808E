'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    fig.add_trace(go.Choroplethmapbox(
        geojson=montreal_data,
        locations=locations,
        z=z_vals,
        showscale=False,
        colorscale=colorscale,
        marker_opacity=0.2,
        marker_line_width=0.5,
        featureidkey="properties.NOM",
        hovertemplate=hover.map_base_hover_template()
    ))
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    for intervention_type in street_df['properties.TYPE_SITE_INTERVENTION'].unique():
        df_subset = street_df[street_df['properties.TYPE_SITE_INTERVENTION'] == intervention_type]
        fig.add_trace(go.Scattermapbox(
            lat=df_subset['geometry.coordinates'].apply(lambda x: x[1]),
            lon=df_subset['geometry.coordinates'].apply(lambda x: x[0]),
            mode='markers',
            marker=dict(size=20),
            name=intervention_type,
            customdata=df_subset[['properties.NOM_PROJET', 'properties.MODE_IMPLANTATION', 'properties.OBJECTIF_THEMATIQUE']],
            hovertemplate=hover.map_marker_hover_template(intervention_type)
        ))
    return fig
