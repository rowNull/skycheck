from weather import get_weather

if __name__ == "__main__":
    userCity = input("\nEnter city name (or type 'exit' to quit): ")
    while(userCity.lower() != 'exit'):
        try:
            data = get_weather(userCity)
            print(f"\nWeather in {data['city']}, {data['country']}:")
            print(f"🌡️ Temperature: {data['temperature']['temp_f']}°F / {data['temperature']['temp_c']}°C")
            print(f"💧 Humidity: {data['humidity']}%")
            print(f"🌤️ Condition: {data['condition']['text']}")
            print(f"💨 Wind: {data['wind']} mph")

        except ValueError as e:
            print(e)
        

        userCity = input("\nEnter city name (or type 'exit' to quit): ")
