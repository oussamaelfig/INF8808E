import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    fig.add_trace(go.Choroplethmapbox(
        geojson=montreal_data,
        locations=locations,
        z=z_vals,
        showscale=False,
        colorscale=colorscale,
        marker_opacity=0.2,
        marker_line_width=0.5,
        featureidkey="properties.NOM",
        hovertemplate="<b>%{properties.NOM}</b><extra></extra>"
    ))

    fig.update_layout(
        mapbox_style="light",
        mapbox_zoom=10,        
        mapbox_center={"lat": 45.5017, "lon": -73.5673} 
    )

    return fig

def add_scatter_traces(fig, street_df):
    for intervention_type in street_df['properties.TYPE_SITE_INTERVENTION'].unique():
        df_subset = street_df[street_df['properties.TYPE_SITE_INTERVENTION'] == intervention_type]
        
        hover_texts = df_subset['properties.NOM_PROJET'].tolist()

        fig.add_trace(go.Scattermapbox(
            lat=df_subset['geometry.coordinates'].apply(lambda x: x[1]),
            lon=df_subset['geometry.coordinates'].apply(lambda x: x[0]),
            mode='markers',
            marker=dict(size=20),
            name=intervention_type,
            hoverinfo='text',
            text=hover_texts, 
            customdata=df_subset[['properties.NOM_PROJET', 'properties.MODE_IMPLANTATION', 'properties.OBJECTIF_THEMATIQUE']]
        ))
    return fig

