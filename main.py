import sys
import json

sys.path.append("/Users/ymgmac/Documents/WI/WI/get_course")
sys.path.append("/Users/ymgmac/Documents/WI/WI/get_weather_api")
sys.path.append("/Users/ymgmac/Documents/WI/WI/get_kmo")

# import numpy as np
# import pandas as pd

from print_course_info import print_course
from get_course_info import get_course_info
from get_coordinates import get_coord_lat_lng
# from get_weather_srt_ncst import get_weather_srt_ncst
# from get_weather_real_time import get_weather_real_time
# from get_weather_forecast import get_weather_forecast
# from get_weather_history import get_weather_history
from get_weather_information import get_weather_information

argv_list = sys.argv[1:]
depart = argv_list[0]
arrive = argv_list[1]

# Get coordinates from the input data(Just for information) 
depart_lat,depart_lng = get_coord_lat_lng(depart)
arrive_lat,arrive_lng = get_coord_lat_lng(arrive)
print("출발지 이름:",depart,"위도/경도:",depart_lat,depart_lng)
print("도착지 이름:",arrive,"위도/경도:",arrive_lat,arrive_lng)

# Get course info
depart_lat_lng, depart_address, arrive_lat_lng, arrive_address, course_lst = get_course_info(depart, arrive)

# Print course info
# - This will be replaced to ETL procedure soon
#print_course(depart, arrive)

# Weather info
# KMO Ver.
#depart_weather_info = get_weather_srt_ncst(depart_lng,depart_lat)
#arrive_weather_info = get_weather_srt_ncst(arrive_lng,arrive_lat)

get_weather_information(depart,2,2)

get_weather_information(arrive,2,2)

