import pandas as pd

TITLES = {
    # pylint: disable=line-too-long
    '1. Noyau villageois': 'Noyau villageois',
    '2. Rue commerciale de quartier, d’ambiance ou de destination': 'Rue commerciale de quartier, d’ambiance ou de destination', # noqa : E501
    '3. Rue transversale à une rue commerciale': 'Rue transversale à une rue commerciale', # noqa : E501
    '4. Rue bordant un bâtiment public ou institutionnel  (tels qu’une école primaire ou secondaire, un cégep ou une université, une station de métro, un musée, théâtre, marché public, une église, etc.)': 'Rue bordant un bâtiment public ou institutionnel', # noqa : E501
    '5. Rue en bordure ou entre deux parcs ou place publique': 'Rue en bordure ou entre deux parcs ou place publique', # noqa : E501
    '6. Rue entre un parc et un bâtiment public ou institutionnel': 'Rue entre un parc et un bâtiment public ou institutionnel', # noqa : E501
    '7. Passage entre rues résidentielles': 'Passage entre rues résidentielles'
}


def to_df(data):
    my_df = pd.json_normalize(data['features'])
    return my_df


def update_titles(my_df):
    my_df['properties.TYPE_SITE_INTERVENTION'] = my_df['properties.TYPE_SITE_INTERVENTION'].map(TITLES)
    return my_df


def sort_df(my_df):
    my_df = my_df.sort_values(by='properties.TYPE_SITE_INTERVENTION')
    return my_df


def get_neighborhoods(montreal_data):
    neighborhoods = [feature['properties']['NOM'] for feature in montreal_data['features']]
    return neighborhoods
