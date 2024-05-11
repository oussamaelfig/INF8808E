'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Generates the hover template for the tooltips in the bar chart.

        Args:
            name: The player's name for which the hover is being created.
            mode: The current display mode ('count' or 'percent')

        Returns:
            A string that defines the custom HTML for the hover tooltip.
    '''
    if mode == MODES['count']:
        line_info = '<b>%{y} lines</b>'
    else:  # mode == MODES['percent']
        line_info = '<b>%{y:.2f}% of lines</b>'

    return f'''
        <b>{name}</b><br>
        <span style="font-size: 16px; font-family: Grenze Gotish, serif; color: black;">
            {line_info}
        </span>
    '''
