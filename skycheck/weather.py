import requests
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

        return {
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