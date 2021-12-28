import os
import json
import pickle

import googlemaps
from pathlib import Path


def get_coord(place, is_save=False):
    '''

    :param place:
    :param is_save:
    :return:
    '''
    path = Path(os.getcwd())

    # Read GCP key (be private!)
    with open(f"{str(path.parent.absolute())}/google_key.json", "r") as client_json:
        client = json.load(client_json)

    # Make inputs
    key = client['key']

    # Return location result
    # - we could save this as pkl file
    gmaps = googlemaps.Client(key=key)
    geocode_result = gmaps.geocode(place, language='ko')[0]

    if is_save:
        with open(f'./coords_data/coords_{place}.pkl', 'wb') as f:
            pickle.dump(geocode_result, f)

    return geocode_result


def get_coord_address(place, is_save=False):
    '''

    :param place:
    :param is_save:
    :return: sting
    '''
    geocode_result = get_coord(place)
    geocode_keys = list(geocode_result.keys())

    return geocode_result[geocode_keys[1]]


def get_coord_lat_lng(place, is_save=False):
    '''

    :param place:
    :param is_save:
    :return: list
    '''
    geocode_result = get_coord(place)
    geocode_keys = list(geocode_result.keys())

    lat_lng_dict = geocode_result[geocode_keys[2]]['viewport']['northeast']
    lat = lat_lng_dict['lat']
    lng = lat_lng_dict['lng']

    return [str(lat), str(lng)]
