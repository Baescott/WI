import numpy as np

DEGRAD: float = np.pi / 180


def lambert_projection(lng, lat, map_info):
    re = map_info['Re'] / map_info['grid']
    slat1 = map_info['slat1'] * DEGRAD
    slat2 = map_info['slat2'] * DEGRAD
    lng0 = map_info['lng0'] * DEGRAD
    lat0 = map_info['lat0'] * DEGRAD

    sn = np.tan(np.pi * 0.25 + slat2 * 0.5) / np.tan(np.pi * 0.25 + slat1 * 0.5)
    sn = np.log(np.cos(slat1) / np.cos(slat2)) / np.log(sn)
    sf = np.tan(np.pi * 0.25 + slat1 * 0.5)
    sf = pow(sf, sn) * np.cos(slat1) / sn
    ro = np.tan(np.pi * 0.25 + lat0 * 0.5)
    ro = re * sf / pow(ro, sn)

    ra = np.tan(np.pi * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lng * DEGRAD - lng0
    if theta > np.pi:
        theta -= 2 * np.pi
    if theta < -np.pi:
        theta += 2 * np.pi
    theta *= sn

    x: float = (ra * np.sin(theta)) + map_info['xo']
    y: float = (ro - ra * np.cos(theta)) + map_info['yo']

    return x, y
