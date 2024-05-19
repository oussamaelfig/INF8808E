'''
    Creates the theme to be used in our bar chart.
'''
import plotly.graph_objects as go
import plotly.io as pio

THEME = {
    'color_scale': 'plotly',  
    'background_color': '#ebf2fa',
    'font_family': 'Montserrat',
    'font_color': '#898989',
    'label_font_size': 16,
    'label_background_color': '#ffffff'
}


def create_template():
    '''
        Adds a new layout template to Plotly's templates based on THEME settings.
    '''
    custom_template = go.layout.Template()

    custom_template.layout = go.Layout(
        colorway=pio.templates[THEME['color_scale']].layout.colorway,
        paper_bgcolor=THEME['background_color'],
        plot_bgcolor=THEME['background_color'],
        font=dict(
            family=THEME['font_family'],
            color=THEME['font_color'],
            size=THEME['label_font_size']
        ),
        hoverlabel=dict(
            bgcolor=THEME['label_background_color'],
            font_size=THEME['label_font_size'],
            font_color=THEME['font_color']
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False
        )
    )

    pio.templates['custom_theme'] = custom_template
    pio.templates.default = 'custom_theme'
