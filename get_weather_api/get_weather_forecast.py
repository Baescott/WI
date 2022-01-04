import os
import json

from pathlib import Path

from weatherapi.weatherapi_client import WeatherapiClient
from WI.get_course.get_coordinates import get_coord_lat_lng


def get_weather_forecast(place, days):
    """

    :param place:
    :param days: Number of days of weather forecast. Value ranges from 1 to 10
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

    result = ap_is_controller.get_forecast_weather(q, days, lang)
    return result
