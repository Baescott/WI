import os
import json
import datetime

from get_weather_real_time import get_weather_real_time
from get_weather_forecast import get_weather_forecast
from get_weather_history import get_weather_history

def get_weather_information(place,days_before,days_after):
    """

    :param place:
    :return:
    """
    dt_before=datetime.datetime.now()-datetime.timedelta(days=days_before)

    weather_real    =get_weather_real_time(place)
    weather_history =get_weather_history(place, dt_before)
    weather_forecast=get_weather_forecast(place, days_after)

    #Just for test
    print(weather_real.location.tz_id)
    print(weather_real.current.temp_c)
    print(weather_real.current.condition.text)
    print(weather_real.current.wind_mph)
    print(weather_real.current.wind_dir)
    print(weather_real.current.precip_mm)
    print(weather_real.current.humidity)
    print(weather_real.current.cloud)
    print(weather_real.current.feelslike_c)
    print(weather_real.current.air_quality.pm10)

    #should have check aqi
    print(weather_forecast.current.wind_mph)
 


