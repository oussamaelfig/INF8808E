'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''
    fig = px.scatter()
    fig.update_layout(
        dragmode=False,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        plot_bgcolor=THEME['pale_color'],
        paper_bgcolor=THEME['pale_color'],
        xaxis={'visible': False},
        yaxis={'visible': False},
        annotations=[
            dict(
                text="No data to display. Select a cell in the heatmap for more information.",
                x=0.5,
                y=0.5,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(
                    size=16,
                    color=THEME['dark_color']
                ),
                align="center"
            )
        ]
    )
    add_rectangle_shape(fig)
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=0,
        y0=0.4,
        x1=1,
        y1=0.6,
        fillcolor=THEME['pale_color'],
        line=dict(width=0)
    )
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    if len(line_data) == 1:
        fig = px.scatter(line_data, x='Date_Plantation', y='Counts', title=f'Trees planted in {arrond} in {year}')
        fig.update_traces(marker=dict(color=THEME['line_chart_color']))
    else:
        fig = px.line(line_data, x='Date_Plantation', y='Counts', title=f'Trees planted in {arrond} in {year}')
        fig.update_traces(line=dict(color=THEME['line_chart_color']))
    
    if not line_data.empty:
        fig.update_layout(
            xaxis_title=None, 
            yaxis_title="Trees",
            xaxis=dict(
                range=[line_data['Date_Plantation'].min(), line_data['Date_Plantation'].max()]
            )
        )
    
    fig.update_traces(hovertemplate=hover_template.get_linechart_hover_template())
    return fig
