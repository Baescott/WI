import json

if __name__ == "__main__":
    wholeDict = None
    with open("./Agent_Transit_Directions.json", "r") as transitJson:
        wholeDict = dict(json.load(transitJson))

    path = wholeDict["routes"][0]["legs"][0]
    duration_sec = path["duration"]["value"]
    start_geo = path["start_location"]
    end_geo = path["end_location"]

    print("우리 집으로부터 윰네 파라다이스텔 SB 까지의 거리다!!!!!!!!!!!!!!")
    print(duration_sec, "초가 걸린다!!!!!!!!!!!")
    print(start_geo)
    print(end_geo)
    stepList = path["steps"]

    print("경로는 총", len(stepList), "개다!!!!!!!!!!!")
    print("경로는 다음과 같다!!!!!!!!!!!!")
    print("-------------------------")
    step = 0
while step < len(stepList):
    print(stepList[step])
    step = step + 1
