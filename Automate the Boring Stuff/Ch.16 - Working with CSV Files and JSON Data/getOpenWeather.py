#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
APPID = '4aa127bde5c097ed2d11659fb639ac65'  # OpenWeather API ID
import json, requests, sys
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.
# Taken from the website api
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()
# Uncomment to see the raw JSON text:
#print(response.text)
# Load JSON data into a Python variable.
w = json.loads(response.text)
# Print weather descriptions.
print('Current weather in %s:' % (location))
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])

