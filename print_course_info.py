import json

if __name__ == "__main__":
    # Read json formatted course file
    with open("./Agent_Transit_Directions.json", "r") as transit_json:
        whole_dict = dict(json.load(transit_json))

    # Get necessary values from result json file
    path = whole_dict["routes"][0]["legs"][0]
    duration_sec = path["duration"]["value"]
    start_geo = path["start_location"]
    end_geo = path["end_location"]

    # Print results
    # - This will be replaced to ETL procedure soon
    print("우리 집으로부터 윰네 파라다이스텔 SB 까지의 거리다!!!!!!!!!!!!!!")
    print(duration_sec, "초가 걸린다!!!!!!!!!!!")
    print(start_geo)
    print(end_geo)
    step_list = path["steps"]

    print("경로는 총", len(step_list), "개다!!!!!!!!!!!")
    print("경로는 다음과 같다!!!!!!!!!!!!")
    print("-------------------------")
    step = 0

while step < len(step_list):
    print(step_list[step])
    step = step + 1
