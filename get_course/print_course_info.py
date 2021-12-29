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
    print("상암미르웰한올림","부터","파라다이스텔SB","까지의 경로")
    print(duration_sec, "초가 걸립니다.")
    print(start_geo)
    print(end_geo)
    step_list = path["steps"]

    print("경로는 총", len(step_list), "번의 과정이 있으며,")
    print("경로는 다음과 같습니다.")
    print("-------------------------")
    
    step = 0

while step < len(step_list):
    print(step_list[step])
    step = step + 1
