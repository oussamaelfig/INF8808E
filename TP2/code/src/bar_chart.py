'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    fig.update_layout(
        template="simple_white",
        title='Lines per Act',
        dragmode=False,
        barmode='relative'
    )

    return fig



def draw(fig, data, mode):
    '''
        Draws the bar chart based on the mode.

        Args:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.

        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    column = MODE_TO_COLUMN[mode]
    fig = go.Figure(fig)
    for act in data['Act'].unique():
        act_data = data[data['Act'] == act]
        for _, row in act_data.iterrows():
            fig.add_trace(go.Bar(
                x=[row['Player']],
                y=[row[column]],
                name=f'Act {act}',
                hovertemplate=get_hover_template(row['Player'], mode)
            ))

    fig.update_layout(
        xaxis_title="Player",
        yaxis_title=column,
        legend_title="Act",
        hovermode='closest'
    )

    return fig



def update_y_axis(fig, mode):
    '''
        Updates the y-axis title based on the mode.

        Args:
            fig: The figure comprising the bar chart
            mode: Current display mode (count or percent)

        Returns:
            fig: The updated figure
    '''
    y_axis_title = 'Lines (%)' if mode == MODES['percent'] else 'Lines (Count)'
    fig.update_layout(yaxis_title=y_axis_title)
    return fig
