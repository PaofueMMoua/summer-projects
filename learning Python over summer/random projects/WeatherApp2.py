# Units 
# time
# error messages human readable
# 
# different file make it a experience that would be like what would you like and if they say anything but weather then it'll return other things and if it does return weather then talk and ask about things.


import requests
import json
import configparser
from datetime import datetime
from api import api

class Weather:

        # getting the result
        def __init__(self, config, sectionTitle ):
                self.config = config
                self.sectionTitle = sectionTitle
# Getting information
        def _info(self, api_url):
                try:
                        response = requests.get(api_url)
                        response.raise_for_status()  
# Raises an error for bad responses

# checking the response status
                        if response.status_code == 200:
                                new_data = response.json()
# getting the temperature
                                temp = new_data['main']['temp']
                                maxTemp = new_data['main']['temp_max']
                                minTemp = new_data['main']['temp_min']
                                feelsLike = new_data['main']['feels_like']
# getting the wind and the weather
                                windSpd = new_data['wind']['speed']
                                weatherDisc = new_data['weather'][0]['description']
# getting the current time
                                currtime = new_data['dt']
                                sunrise = new_data['sys']['sunrise']
                                sunset = new_data['sys']['sunset']
                                name = new_data['name']
                                country = new_data['sys']['country']
                                temp_check = True
                                if temp_check:
                                        self._printing_result(name, country, temp, feelsLike, maxTemp, minTemp, windSpd, weatherDisc, sunrise, sunset, currtime)
                except requests.exceptions.RequestException as e:
                        raise ValueError(f"\n\n Error fetching data: City name is either spelt wrong or does not exist.\n")
# Printing out the time and information
        def _printing_result(self, name, country, temp, feelsLike, maxTemp, minTemp, windSpd, weatherDisc, sunrise, sunset, currtime):

                print()
                print()
                print()
                print(f'In {name} {country}\n')
# printing the proper information if it is included

                # Checking the configuration settings to determine which
                # information to display based on the specified checks. Here's what each part does:
                if self.config[self.sectionTitle]['tempCheck'].lower() == 'true':
                        self._temp_Printing(name, temp, feelsLike, maxTemp, minTemp)
                if self.config[self.sectionTitle]['windCheck'].lower() == 'true':
                        self._wind_weather(windSpd, weatherDisc)
                if self.config[self.sectionTitle]['timeCheck'].lower() == 'true':
                        self._time(sunrise, sunset, currtime)
# Printing the temperature
        def _temp_Printing(self, name, temp, feelsLike, maxTemp, minTemp):

                # Printing out the current temperature
                # information for a specific city. It formats and displays the following details:
                # - City name: `name`
                # - Current temperature: `temp` (rounded to 2 decimal places)
                # - Feels like temperature: `feelsLike` (rounded to 2 decimal places)
                # - Highest temperature: `maxTemp` (rounded to 2 decimal places)
                # - Lowest temperature: `minTemp` (rounded to 2 decimal places)
                degUnit = 'Celsius'
                if (self.config[self.sectionTitle]['Unit']) == "imperial" or (self.config[self.sectionTitle]['Unit']) == "Imperial":
                        degUnit = 'Fahrenheit'
                print(f'Current Temperature In {name}')
                print(f'Temp    :   {round(temp, 2)} deg {degUnit}')
                print(f"Feels   :   {round(feelsLike, 2)} deg {degUnit}")
                print(f'Highest :   {round(maxTemp, 2)} deg {degUnit}')
                print(f'Low     :   {round(minTemp, 2)} deg {degUnit}\n')
# Printing the wind speed and the weather
        def _wind_weather(self, windSpd, weatherDisc):

                # Checking the unit specified in the configuration file to
                # determine whether to display the wind speed in miles per hour (mph) or meters per
                # second (m/s).
                if (self.config[self.sectionTitle]['Unit']) == "imperial" or (self.config[self.sectionTitle]['Unit']) == "Imperial":
                        print(f"Wind : {round(windSpd, 2)} MPH")
                else:
                        print(f"Wind : {round(windSpd, 2)} M/S")
                print(f'{weatherDisc.title()}\n')
# Printing time
        def _time(self, sunrise, sunset, currtime):

                # Printing out the sunrise time, sunset time,
                # and current time in a human-readable format.
                print(f'Sunrise      : {datetime.fromtimestamp(sunrise).strftime("%I:%M:%S:%p")}')
                print(f'Sunset       : {datetime.fromtimestamp(sunset).strftime("%I:%M:%S:%p")}')
                print(f'Current Time : {datetime.fromtimestamp(currtime).strftime("%I:%M:%S:%p")}\n')
# Running 
        def run(self, api):
# getting the city and the unit from the file

                city = (self.config[self.sectionTitle]['City'])
                unit = (self.config[self.sectionTitle]['Unit'])
# checking for errors within the code

                if unit.lower() != 'imperial' and unit.lower() != 'metric':
                        raise ValueError("\n\nUnit is wrong. Needs to be Imperial or Metric\n")
                try:
                        return self._info(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units={unit}")
                except NameError:
                        raise NameError("City Name is misspelled or missing.")
# Getting the city name from the config file

# weather_resp = Weather(config, sectionTitle)
# weather_resp.run()