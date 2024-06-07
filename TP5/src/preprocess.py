'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import json
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
    features = data['features']
    rows = []
    for feature in features:
        properties = feature['properties']
        coordinates = feature['geometry']['coordinates']
        properties['longitude'] = coordinates[0]
        properties['latitude'] = coordinates[1]
        rows.append(properties)

    return pd.DataFrame(rows)


def update_titles(my_df):
    my_df['TYPE_AXE'] = my_df['TYPE_AXE'].replace(TITLES)
    return my_df



def sort_df(my_df):
    my_df = my_df.sort_values('TYPE_AXE')
    return my_df

def convert_dict_to_dataframe(geojson_dict):
    # This function assumes 'geojson_dict' is a dictionary formatted as GeoJSON
    features = geojson_dict.get('features', [])  # safely get features list or empty list if not present
    # Extract properties and potentially coordinates from each feature
    data_rows = []
    for feature in features:
        properties = feature.get('properties', {})  # safely get properties or empty dict if not present
        if 'geometry' in feature and 'coordinates' in feature['geometry']:  # check if coordinates are present
            properties['coordinates'] = feature['geometry']['coordinates']
        data_rows.append(properties)
    return pd.DataFrame(data_rows)


def get_neighborhoods(montreal_data):
    print("*****")
    
    montreal_df = convert_dict_to_dataframe(montreal_data)


    neighborhoods = montreal_df['NOM'].unique().tolist()
    return neighborhoods

