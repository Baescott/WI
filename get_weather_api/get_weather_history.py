import os
import json

from pathlib import Path

from weatherapi.weatherapi_client import WeatherapiClient
from get_course.get_coordinates import get_coord_lat_lng


def get_weather_history(place, dt):
    """

    :param place:
    :param dt: Date on or after 1st Jan, 2015 in yyyy-MM-dd format
    :return:
    """
    path = Path(os.getcwd())

    # Read Weather API key (be private!)
    with open(f"{str(path.parent.absolute())}/weather_api_key.json", "r") as client_json:
        api_json = json.load(client_json)

    key = api_json['key']
    client = WeatherapiClient(key)

    ap_is_controller = client.ap_is

    q = ','.join(get_coord_lat_lng(place))
    lang = 'ko'

    result = ap_is_controller.get_history_weather(q, dt, lang)
    return result
