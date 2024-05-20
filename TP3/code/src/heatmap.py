'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    fig = px.imshow(data, 
                    labels=dict(x="Year", y="Neighborhood", color="Trees"),
                    x=list(data.columns),
                    y=list(data.index),
                    color_continuous_scale='YlGnBu')
    
    fig.update_layout(dragmode=False)
    fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template())
    return fig
