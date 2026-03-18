import requests
from datetime import datetime
from skycheck.config import API_KEY, API_URL

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city, 
        "aqi": "no"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    if "location" in data:

        location = data["location"]
        current = data["current"]
        date_string = location['localtime'].split(" ", 1)[0]
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        weekday_name = date_obj.strftime("%A")
        



       

        return {
            'weekday': weekday_name,
            'city': location['name'],
            'country': location['country'],
            'temperature' : {
                'temp_f': current['temp_f'],
                'temp_c': current['temp_c'],
                },
            'humidity': current['humidity'],
            'condition':current['condition'],
            'condition_class': get_condition_class(current['condition']['code']),
            'wind': current['wind_mph'],
            }

    else:
        raise ValueError(data['error']['message'])

def get_condition_class(code):
    if code == 1000:
        return "sunny"
    elif 1003 <= code <= 1030:
        return "cloudy"
    elif 1135 <= code <= 1147:
        return "foggy"
    elif  1150 <= code <= 1201 or 1240 <= code <= 1264:
        return "rainy"
    elif 1066 <= code <= 1117 or 1204 <= code <= 1237:
        return "snowy"
    elif 1273 <= code <= 1282:
        return "stormy"
    else:
        return "cloudy"