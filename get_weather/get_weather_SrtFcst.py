import json
import ssl
import urllib.request
from datetime import datetime, timedelta

from lambert import lambert_projection

key = 'm%2B7xkBjgRbBpjVrmx332C%2B%2FpYDPxIlzFvA2Y6%2F%2F6ay%2BSlNvJ91WCzlP6pvDiZIMqDcFtj9GwgbDitr%2FrOf1P5A%3D%3D'
base_date = datetime.today().strftime('%Y%m%d')  # 날짜
base_time = (datetime.today() - timedelta(hours=1)).strftime('%H') + '00'  # 시간 / API 공개시간이 애매해서 일단은 1시간 전으로
# lat = '37.56313127045668' # 위도
# lng = '126.93375479638536' # 경도

# XY 변환
NX = 149  # X축 격자점 수
NY = 253  # Y축 격자점 수

map_info = dict()
map_info['Re'] = 6371.00877  # 지도반경(km)
map_info['grid'] = 5.0  # 격자간격(km)
map_info['slat1'] = 30.0  # 표준위도 1
map_info['slat2'] = 60.0  # 표준위도 2
map_info['lng0'] = 126.0  # 기준점 경도
map_info['lat0'] = 38.0  # 기준점 위도
map_info['xo'] = 210 / map_info['grid']  # 기준점 X좌표
map_info['yo'] = 675 / map_info['grid']  # 기준점 Y좌표
map_info['first'] = 0  # 시작여부 (0 = 시작)


def get_weather_SrtFcst(lng, lat):
    lng1 = float(lng)
    lat1 = float(lat)

    X, Y = lambert_projection(lng1, lat1, map_info)
    X = int(X + 1.5)
    Y = int(Y + 1.5)

    url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst" + \
          f"?serviceKey={key}&numOfRows=100&pageNo=1&dataType=JSON" + \
          f"&base_date={base_date}&base_time={base_time}&nx={X}&ny={Y}"

    request = urllib.request.Request(url)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, context=context)
    response_text = response.read().decode('utf-8')
    response_json = json.loads(response_text)

    '''
    T1H	기온
    RN1	1시간 강수량
    SKY	하늘상태
    UUU	동서바람성분
    VVV	남북바람성분
    REH	습도
    PTY	강수형태
    LGT	낙뢰
    VEC	풍향
    WSD	풍속
    '''

    return response_json
