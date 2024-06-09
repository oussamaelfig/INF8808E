from dash import html, dcc

def no_clicks(style):
    style['visibility'] = 'hidden'
    return [], style

def map_base_clicked(title, mode, theme, style):
    style['visibility'] = 'hidden'
    return [], style 

def map_marker_clicked(figure, curve, point, title, mode, theme, style):
    data = figure['data'][curve]
    custom_data = data['customdata'][point]
    
    title = custom_data[0]  
    mode = custom_data[1] 
    theme_str = custom_data[2]  

    if not theme_str:
        theme_content = html.Div("No thematic information available")
    else:
        theme_items = theme_str.split('\n')
        theme_content = html.Ul([html.Li(item) for item in theme_items if item.strip()], style={'padding-left': '20px', 'list-style-type': 'disc'})

    style['visibility'] = 'visible'
    style['display'] = 'block'

    return title, mode, theme_content, style
