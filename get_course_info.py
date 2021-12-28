# coding: utf-8
import ssl
import json

import urllib.request

if __name__ == "__main__":
    client = None
    with open("./google_key.json", "r") as clientJson:
        client = json.load(clientJson)

    origin = "37.565211608460935,126.90448920622298"
    destination = "37.571270658174626,126.9348124477444"
    mode = "transit"
    departure_time = "now"
    key = client["key"]

    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}" + \
          f"&destination={destination}" + \
          f"&mode={mode}" + \
          f"&departure_time={departure_time}" + \
          f"&language=ko&key={key}"

    request = urllib.request.Request(url)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, context=context)
    responseText = response.read().decode('utf-8')
    responseJson = json.loads(responseText)

    with open("./Agent_Transit_Directions.json", "w") as rltStream:
        json.dump(responseJson, rltStream)
