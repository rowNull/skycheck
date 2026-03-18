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
            'wind': current['wind_mph'],
            }

    else:
        raise ValueError(data['error']['message'])