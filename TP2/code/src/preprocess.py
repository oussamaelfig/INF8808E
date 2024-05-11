'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    act_player_lines = my_df.groupby(['Act', 'Player']).size().reset_index(name='LineCount')
    
    # Calculate total lines per act
    act_total_lines = act_player_lines.groupby('Act')['LineCount'].sum().reset_index(name='TotalLines')
    
    merged_df = pd.merge(act_player_lines, act_total_lines, on='Act')
    merged_df['LinePercent'] = (merged_df['LineCount'] / merged_df['TotalLines']) * 100
    
    # Drop the total lines as it's no longer needed
    merged_df.drop(columns=['TotalLines'], inplace=True)
    
    return merged_df



def replace_others(my_df):
    # Get the top 5 players
    top_players = my_df.groupby('Player')['LineCount'].sum().nlargest(5).index
    
    others_df = my_df[~my_df['Player'].isin(top_players)]
    top_df = my_df[my_df['Player'].isin(top_players)]
    
    # Sum the 'others' lines
    others_summed = others_df.groupby('Act').agg({'LineCount': 'sum', 'LinePercent': 'sum'}).reset_index()
    others_summed['Player'] = 'OTHER'
    
    final_df = pd.concat([top_df, others_summed], ignore_index=True)
    
    return final_df



def clean_names(my_df):
    my_df['Player'] = my_df['Player'].str.title()
    return my_df

