'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
from dash import dcc

def no_clicks(style):
    style['visibility'] = 'hidden'  
    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    style['visibility'] = 'hidden'  
    return "Map clicked", "No specific mode", "No theme", style


def map_marker_clicked(figure, curve, point, title, mode, theme, style):

    data = figure['data'][curve]
    hover_texts = data['hovertext']

    if hover_texts and len(hover_texts) > point:
        title = hover_texts[point]  
    else:
        title = "todo"

    mode = "todo"
    theme = "todo"

    style['visibility'] = 'visible'  
    return title, mode, theme, style

