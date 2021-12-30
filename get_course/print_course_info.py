import os
import json
import pickle


def print_course(depart, arrive):
    '''

    :param depart:
    :param arrive:
    :return:

    '''
    # Read json formatted course file
    with open(f"./get_course/course_data/from_{depart}_to_{arrive}.json", "r") as transit_json:
        whole_dict = dict(json.load(transit_json))

    # Get necessary values from result json file
    path = whole_dict["routes"][0]["legs"][0]
    duration_sec = path["duration"]["value"]
    

    # Print results
    # - This will be replaced to ETL procedure soon
    print("==========",depart,"부터",arrive,"까지의 경로","==========")
    print((duration_sec/60)//60,"시간 ",(duration_sec/60)%60,"분이 걸립니다.")
    step_list = path["steps"]
    print("경로는 총", len(step_list), "번의 과정이 있으며,")
    print("경로는 다음과 같습니다.")
    print("-------------------------")


    step = 0
    while step < len(step_list):
        print(step_list[step])
        step = step + 1