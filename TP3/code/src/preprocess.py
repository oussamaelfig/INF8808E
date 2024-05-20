'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    dataframe = dataframe[(dataframe['Date_Plantation'].dt.year >= start) & (dataframe['Date_Plantation'].dt.year <= end)]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    dataframe['Year'] = dataframe['Date_Plantation'].dt.year
    yearly_counts = dataframe.groupby(['Arrond_Nom', 'Year']).size().reset_index(name='Counts')
    return yearly_counts


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    heatmap_df = yearly_df.pivot(index='Arrond_Nom', columns='Year', values='Counts').fillna(0)
    return heatmap_df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    daily_data = dataframe[(dataframe['Arrond_Nom'] == arrond) & (dataframe['Date_Plantation'].dt.year == year)]
    daily_data.set_index('Date_Plantation', inplace=True)
    daily_counts = daily_data.resample('D').size().reset_index(name='Counts')
    # Filter out leading and trailing zeros to focus on the active period
    first_non_zero = daily_counts['Counts'].ne(0).idxmax()
    last_non_zero = daily_counts['Counts'].iloc[::-1].ne(0).idxmax()
    daily_counts = daily_counts.iloc[first_non_zero:last_non_zero+1]
    
    daily_counts['Date_Plantation'] = daily_counts['Date_Plantation'].dt.date
    
    return daily_counts
