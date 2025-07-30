import requests
import json
import configparser
import time

class Weather:

# getting the result
    def __init__(self, config, sectionTitle ):
        self.config = config
        self.sectionTitle = sectionTitle

    def _result(self, api_url):
        response = requests.get(api_url)

# checking the response status

        if response.status_code == 200:
            new_data = response.json()

# getting the temperature

            temp = new_data['main']['temp']
            maxTemp = new_data['main']['temp_max']
            minTemp = new_data['main']['temp_min']

# getting the wind and the weather

            windSpd = new_data['wind']['speed']
            weatherDisc = new_data['weather'][0]['description']

# getting the current time

            currtime = new_data['dt']
            sunrise = new_data['sys']['sunrise']
            sunset = new_data['sys']['sunset']

            name = new_data['name']

# Printing out the time and information
        print()
        print()
        print()
        print(f'In {name}\n')

# printing the temperature

        print(f'Temp    :   {round(((9/5) * (temp - 273.15) + 32), 2)} deg F')
        print(f'Highest :   {round(((9/5) * (maxTemp - 273.15) + 32), 2)} deg F')
        print(f'Low     :   {round(((9/5) * (minTemp - 273.15) + 32), 2)} deg F\n')

# printing the wind speed and the weather

        print(f"Wind : {round((windSpd * 2.237), 2)} mph")
        print(f'{weatherDisc.title()}\n')

# printing time

        print(f'Sunrise      : {time.ctime(sunrise)}')
        print(f'Sunset       : {time.ctime(sunset)}')
        print(f'Current Time : {time.ctime(currtime)}\n')

# running 

    def run(self):
        city = (self.config[self.sectionTitle]['City'])
        print(type(city))
        api = "b097d68cae69aff3f77b5f62165a3566"
        return self._result(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}")

# getting the city name from the config file

configName = 'weatherConfig.ini'
sectionTitle = 'City'
config = configparser.ConfigParser()
config.read(configName)

weather_resp = Weather(config, sectionTitle)
print(weather_resp.run())