# coding: utf-8
import ssl
import json

import urllib.request

if __name__ == "__main__":
    # Read GCP key (be private!)
    with open("./google_key.json", "r") as client_json:
        client = json.load(client_json)

    # Make inputs
    # - `origin` and `destination` will be replaced to sys.argv
    origin = "37.565211608460935,126.90448920622298"
    destination = "37.571270658174626,126.9348124477444"
    mode = "transit"
    departure_time = "now"
    key = client["key"]

    # Make API url with inputs
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}" + \
          f"&destination={destination}" + \
          f"&mode={mode}" + \
          f"&departure_time={departure_time}" + \
          f"&language=ko&key={key}"

    # Download course result as json file
    request = urllib.request.Request(url)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, context=context)
    response_text = response.read().decode('utf-8')
    response_json = json.loads(response_text)

    with open("./Agent_Transit_Directions.json", "w") as rltStream:
        json.dump(response_json, rltStream)
