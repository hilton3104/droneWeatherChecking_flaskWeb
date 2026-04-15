import requests
import wind_crawler as wc
from datetime import datetime

def get_windSpeed(location):
    wind_speed_data = wc.get_hko_wind_data()
    if not wind_speed_data:
        return 0.0
    return wind_speed_data[location]

def get_weatherInfo():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    params = {
        "dataType": "rhrread",
        "lang": "tc"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_night_time():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/opendata.php"
    params = {
        "dataType": "SRS",
        "rformat": "json",
        "year": datetime.now().year,
        "month": datetime.now().month,
        "day": datetime.now().day
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["data"][0][1], data["data"][0][3]

def get_current_time():
    return datetime.now().strftime("%H:%M")


def check_drone_safety(wind_speed, is_rainy, current_time, af_night_time, bf_night_time):
    is_daytime = af_night_time < current_time < bf_night_time

    if wind_speed < 15 and not is_rainy and is_daytime:
        return "✅ Safe to fly the drone"
    elif wind_speed < 30 and not is_rainy and is_daytime:
        return "⚠️ Warning, fly with caution"
    else:
        return "❌ Not safe to fly the drone"