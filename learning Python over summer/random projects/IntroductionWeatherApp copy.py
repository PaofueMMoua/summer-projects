import WeatherApp2
import re
import sys
import os
import configparser
from api import api
configName = 'weatherConfig.ini'
secTitle = 'CityInfo'
UserName_input = str(input('\nHello, whats your name\n')).capitalize()
Yes_Or_No = '(Y / N)'
config = configparser.ConfigParser()
if os.path.exists(configName):
    try:
        config.read(configName)
    except configparser.Error as e:
        print(f"Error reading configuration file: {e}. Using default settings.")
else:
    print(f"Configuration file '{configName}' not found. Creating a default configuration.")
    config.add_section(secTitle)
    config[secTitle]['City'] = 'New York'
    config[secTitle]['Unit'] = 'metric'
    config[secTitle]['tempcheck'] = 'False'
    config[secTitle]['windcheck'] = 'False'
    config[secTitle]['timecheck'] = 'False'
    config.read(configName)
def get_city():
    while True:
        city = str(input("\nPlease enter the name of the city you want to check for (e.g., 'New York').\n"))
        while not city:
            try:
                city = str(input("City name has to be a valid city.\n Please enter the name of the city you want to check for (e.g., 'New York').\n"))
            except ValueError as e:
                print(e)
                sys.exit(0)
        if city.replace(' ', '') != '':
            if re.match(r"^[a-zA-Z\s]+$", city):
                checkCity = str(input(f"\nis {city} the correct city {Yes_Or_No}\n"))
                while checkCity.lower().replace(' ','') == 'y' or 'yes':
                    return city
            else:
                print("Invalid city name. Please enter only letters and spaces.")
        else:
            print("Please don't leave only spaces or blank")
def get_unit():
    while True:
        unit = str(input('What kind of unit would you like to use? (Imperial or Metric)\n'))
        if unit.lower().replace(' ','') in ('imperial', 'metric'):
            checkUnit = str(input(f'\n\nis {unit} the correct unit you chose {Yes_Or_No}\n'))
            while checkUnit.lower().replace(' ','') != 'y':
                unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
                checkUnit = str(input(f'\n\nis {unit} the correct unit you chose {Yes_Or_No}\n'))
            return unit
        else:
            print('Please enter a valid unit like (Imperial or Metric)')
def get_User_Input(UserName_input):
    user_Query_Input = str(input(f'\nSo {UserName_input}, how can I help you?\n\n')).lower()
    if 'weather' in user_Query_Input:
        city = get_city()
        unit = get_unit()
        weather_info_request = input("\nWhat about the weather would you like to know about? (e.g., temp, wind, time, sun)\n\n").lower()
        config_Weather_Settings_(city, unit, config, weather_info_request)
    elif 'time' in user_Query_Input or 'clock' in user_Query_Input:
        city = get_city()
        config_Weather_Settings_(city, 'metric', config, 'time')
    elif 'temp' in user_Query_Input:
        city = get_city()
        unit = get_unit()
        config_Weather_Settings_(city, unit, config, 'temp')
    elif "help" in user_Query_Input:
        print('\nMost common responses are weather, time, and temp\n')
        get_User_Input(UserName_input)
    else:
        print("Unfortunately I can't help you with this inquiry but I can help with time or weather.")
        while True:
            choice = str(input(f'\n\nDo you want to ask another question {Yes_Or_No}\n\n'))
            if choice.lower().replace(' ','') == 'y':
                get_User_Input(UserName_input)
            elif choice.lower().replace(' ','') == 'n':
                sys.exit(0)
            else:
                print(f'Please give a response of {Yes_Or_No}')
def config_Weather_Settings_(city, unit, config, weather_info_request):
    if city == '' or unit == '':
        ValueError("Your city or unit is blank try again")
        sys.exit(0)
    config[secTitle]['City'] = city
    config[secTitle]['Unit'] = unit
    config[secTitle]['tempcheck'] = 'True' if 'temp' in weather_info_request else 'False'
    config[secTitle]['windcheck'] = 'True' if 'weather' in weather_info_request or 'wind' in weather_info_request else 'False'
    config[secTitle]['timecheck'] = 'True' if 'time' in weather_info_request or 'sun' in weather_info_request else 'False'
    try:
        with open(configName, 'w') as configfile:
            config.write(configfile)
    except IOError as e:
        print(f"Error writing to the configuration file: {e}.  Your settings may not be saved.")
    try:
        temp = WeatherApp2.Weather(config, secTitle)
        print(temp.run(api))
        final_question = str(input(f'Do you want to know more about another city? \n{Yes_Or_No}')).lower()
        if final_question == 'y':
            get_User_Input(UserName_input)
        else:
            print('exit')
            sys.exit(0)
    except Exception as e:
        print(e)
    else:
        print('completed')
get_User_Input(UserName_input)