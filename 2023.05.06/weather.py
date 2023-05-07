import sys
import requests

def get_weather(api_key, city, country):
    # Send a GET request to the OpenWeatherMap API
    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={city},{country}&appid={api_key}&units=standard"
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code != 200:
        print("Sorry, something went wrong. Please try again later.")
        print(response.text)
        return

    # Parse the JSON response
    data = response.json()

    # Print the weather information
    print(f"Current weather in {city}, {country}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels like: {data['main']['feels_like']}°C")
    print(f"Weather conditions: {data['weather'][0]['description']}")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python weather.py <city> <country>")
    else:
        api_key = "07eca7a17e135bf9a8af87cc3bb32c6e"
        city = sys.argv[1]
        country = sys.argv[2]
        get_weather(api_key, city, country)
