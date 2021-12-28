import os
import json
import pickle

import googlemaps
from pathlib import Path


if __name__ == "__main__":
    path = Path(os.getcwd())

    # Read GCP key (be private!)
    with open(f"{str(path.parent.absolute())}/google_key.json", "r") as client_json:
        client = json.load(client_json)

    # Make inputs
    # - `place` will be replaced to sys.argv
    place = "삼성전자서초사옥"
    key = client['key']

    # Download location result as pkl file
    gmaps = googlemaps.Client(key=key)
    geocode_result = gmaps.geocode(place, language='ko')
    # print(geocode_result)

    with open('./coords_data/geocode_result.pkl', 'wb') as f:
        pickle.dump(geocode_result, f)
