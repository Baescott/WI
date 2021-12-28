import sys

# import numpy as np
# import pandas as pd

from get_course.get_course_info import get_course_info

argv_list = sys.argv[1:]
depart = argv_list[1]
arrive = argv_list[2]

depart_lat_lng, depart_address, arrive_lat_lng, arrive_address, course_lst = get_course_info(depart, arrive)

