
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''


import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State

import pandas as pd

import preprocess
import bar_chart

from template import create_template
from modes import MODES


app = dash.Dash(__name__)
app.title = 'TP2 | INF8808'


def prep_data():
    '''
        Imports the .csv file and does some preprocessing.

        Returns:
            A pandas dataframe containing the preprocessed data.
    '''
    dataframe = pd.read_csv('./assets/data/romeo_and_juliet.csv')

    proc_data = preprocess.summarize_lines(dataframe)
    proc_data = preprocess.replace_others(proc_data)
    proc_data = preprocess.clean_names(proc_data)

    return proc_data


def init_app_layout(figure):
    '''
        Generates the HTML layout representing the app.

        Args:
            figure: The figure to display.

        Returns:
            The HTML structure of the app's web page.
    '''
    return html.Div(className='content', children=[
        html.Header(children=[
            html.H1('Who\'s Speaking?'),
            html.H2('An analysis of Shakespeare\'s Romeo and Juliet')
        ]),
        html.Main(children=[
            html.Div(className='viz-container', children=[
                dcc.Graph(
                    figure=figure,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=True  # Enable the display mode bar
                    ),
                    className='graph',
                    id='line-chart'
                )
            ])
        ]),
        html.Footer(children=[
            html.Div(className='panel', children=[
                html.Div(id='info', children=[
                    html.P('Use the radio buttons to change the display mode.'),
                    html.P(children=[
                        html.Span('The current mode is : '),
                        html.Span('Count', id='mode')
                    ])
                ]),
                html.Div(children=[
                    dcc.RadioItems(
                        id='radio-items',
                        options=[
                            dict(label=MODES['count'], value=MODES['count']),
                            dict(label=MODES['percent'], value=MODES['percent']),
                        ],
                        value=MODES['count']
                    )
                ])
            ])
        ])
    ])



@app.callback(
    [Output('line-chart', 'figure'), Output('mode', 'children')],
    [Input('radio-items', 'value')],
    [State('line-chart', 'figure')]
)
def update_chart(mode, figure):
    '''
        Updates the application after the mode input is modified.

        Args:
            mode: The mode selected in the radio input.
            figure: The figure as it is currently displayed.

        Returns:
            new_fig: The figure to display after the change of inputs.
            mode_text: The new mode text.
    '''
    new_fig = bar_chart.init_figure()
    new_fig = bar_chart.draw(new_fig, data, mode)
    
    mode_text = 'Percent Mode' if mode == MODES['percent'] else 'Count Mode'
    
    return new_fig, mode_text



data = prep_data()
all_players = data['Player'].unique().tolist()

create_template()

fig = bar_chart.init_figure()
fig = bar_chart.draw(fig, data, MODES['count'])  # Default to 'Count' mode

app.layout = init_app_layout(fig)




