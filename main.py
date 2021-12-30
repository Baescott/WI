import sys

# import numpy as np
# import pandas as pd

from get_course.get_course_info import get_course_info
from get_course.get_coordinates import get_coord_lat_lng
from get_course.print_course_info import print_course
from get_weather.get_weather_SrtNcst import get_weather_SrtNcst

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
print_course(depart, arrive)

# Weather info
depart_weather_info = get_weather_SrtNcst(depart_lng,depart_lat)
arrive_weather_info = get_weather_SrtNcst(arrive_lng,arrive_lat)
# - This will be replaced to ETL procedure soon
print(depart_weather_info)
print(arrive_weather_info)