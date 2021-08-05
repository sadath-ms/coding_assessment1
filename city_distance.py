from math import (
    radians,
    cos,
    sin,
    sqrt,
    atan2
)


def city_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    cal = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    distance = R * 2 * atan2(sqrt(cal), sqrt(1 - cal))
    return f'City 1 and City 2 are {round(distance)} km apart'


if __name__ == '__main__':
    print("Insert Latitude and Longitude Separated with ,")
    city1 = input("City1: ").split(',')
    city2 = input("City2: ").split(',')
    # cd = city_distance(51.5074, 0.1278, 48.8566, 2.3522)
    cd = city_distance(city1[0], city1[1], city2[0], city2[1])
    print(cd)