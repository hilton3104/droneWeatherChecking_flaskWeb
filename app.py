from flask import Flask, render_template, request, jsonify
import function as func
from datetime import datetime

app = Flask(__name__)



@app.route('/api/weather')
def api_weather():
    location =  request.args.get('location', '京士柏')
    district = None
    if location == "京士柏":
        district = "油尖旺"
    elif location == "大美督":
        district = "大埔"
    elif location == "西貢":
        district = "西貢"
    temp = 0
    is_rainy = False

    wind_speed = func.get_windSpeed(location)
    weather_info = func.get_weatherInfo()
    current_time = func.get_current_time()
    after_night_time, before_night_time = func.get_night_time()
    current_dt = datetime.strptime(current_time, "%H:%M")
    af_night_dt = datetime.strptime(after_night_time, "%H:%M")
    bf_night_dt = datetime.strptime(before_night_time, "%H:%M")

    for i in weather_info['temperature']['data']:
        if i['place'] == location:
            temp = i['value']
            break
    
    
    for i in weather_info['rainfall']['data']:
        if i['place'] == district and i['max'] > 0:
            is_rainy = True
            break

    message = func.check_drone_safety(wind_speed, is_rainy, current_dt, af_night_dt, bf_night_dt)

    return jsonify({
        "location": location,
        "wind_speed": wind_speed,
        "temperature": temp,
        "is_rainy": is_rainy,
        "current_time": current_time,
        "safety_message": message
    })


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)