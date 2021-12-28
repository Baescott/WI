# coding: utf-8
import os
import ssl
import json
import datetime

import urllib.request
from pathlib import Path

from get_coordinates import get_coord_lat_lng


def get_course_json(depart, arrive):
    '''

    :param depart:
    :param arrive:
    :return response_json: ends with .json
    '''
    path = Path(os.getcwd())

    # Read GCP key (be private!)
    with open(f"{str(path.parent.absolute())}/google_key.json", "r") as client_json:
        client = json.load(client_json)

    # Get XY coordinates of origin and dest
    depart_lat_lng = ','.join(get_coord_lat_lng(depart))
    arrive_lat_lng = ','.join(get_coord_lat_lng(arrive))

    # Make inputs
    mode = "transit"
    departure_time = "now"
    key = client["key"]

    # Make API url with inputs
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={depart_lat_lng}" + \
          f"&destination={arrive_lat_lng}" + \
          f"&mode={mode}" + \
          f"&departure_time={departure_time}" + \
          f"&language=ko&key={key}"

    # Download course result as json file
    # - the name of json file should be modified later
    request = urllib.request.Request(url)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, context=context)
    response_text = response.read().decode('utf-8')
    response_json = json.loads(response_text)

    # now = str(datetime.datetime.now()).split('.')[0]
    with open(f"./course_data/from_{depart}_to_{arrive}.json", "w") as rltStream:
        json.dump(response_json, rltStream)

def get_course_info(depart, arrive):
    '''

    :param depart:
    :param arrive:
    :return:
    '''
    get_course_json(depart, arrive)

    with open(f"./course_data/from_{depart}_to_{arrive}.json", "r") as transit_json:
        whole_dict = dict(json.load(transit_json))

    # Get necessary values from result json file
    path = whole_dict["routes"][0]["legs"][0]

    depart_lat_lng = path["start_location"]
    depart_address = path["start_address"]
    arrive_lat_lng = path["end_location"]
    arrive_address = path["end_address"]
    course_lst = path["steps"]

    return depart_lat_lng, depart_address, arrive_lat_lng, arrive_address, course_lst
