import requests
import json
import time
import pyinputplus as pyip

api_key = 'a9c5b45ad418511766ffb4ef59b1756d'

url = "http://api.openweathermap.org/data/2.5/weather"

favorite_cities = []

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None

def add_favorite_city():
    city_name = input("Enter the city name you want to add to favorites: ")
    favorite_cities.append(city_name)
    print(f"{city_name} added to favorites!")

def remove_favorite_city():
    if not favorite_cities:
        print("Your favorite cities list is empty.")
        return

    print("Your favorite cities:")
    for i, city in enumerate(favorite_cities):
        print(f"{i + 1}. {city}")

    while True:
        try:
            city_index = int(input("Select the number of the city you want to remove: ")) - 1
            if 0 <= city_index < len(favorite_cities):
                removed_city = favorite_cities.pop(city_index)
                print(f"{removed_city} removed from favorites!")
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_favorites():
    if not favorite_cities:
        print("Your favorite cities list is empty.")
    else:
        for i, city in enumerate(favorite_cities, start=1):
            print(f"{i}. {city}")

def main():
    while True:
        print("\nWeather Checking Application")
        print("1. Check weather by city name")
        print("2. Add a city to favorites")
        print("3. Remove a city from favorites")
        print("4. Display favorite cities")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            city_name = input("Enter the city name: ")
            weather_data = get_weather(city_name)
            if weather_data:
                if "weather" in weather_data and "main" in weather_data:
                    print(f"Weather in {city_name}: {weather_data['weather'][0]['description']}")
                    print(f"Temperature: {weather_data['main']['temp']}°C")
                    print(f"Humidity: {weather_data['main']['humidity']}%")
                else:
                    print("Invalid weather data. Please try again.")
        elif choice == '2':
            add_favorite_city()
        elif choice == '3':
            remove_favorite_city()
        elif choice == '4':
            display_favorites()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


        refresh_interval = 15 * (int(time.time()) % 2)
        print(f"Refreshing in {refresh_interval} seconds...")
        time.sleep(refresh_interval)

if __name__ == "__main__":
    main()