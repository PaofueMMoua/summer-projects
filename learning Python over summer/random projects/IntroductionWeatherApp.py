import WeatherApp2
import re
import os
import configparser
import requests
from api import api

configName = 'weatherConfig.ini'
secTitle = 'CityInfo'

UserName_input = str(input('\nHello, whats your name\n')).capitalize()
Yes_Or_No = '(Y / N)'

config = configparser.ConfigParser()

# if the configuration file named `weatherConfig.ini` exists in the current directory using `os.path.exists(configName)`. If the file exists, it attempts to read the configuration settings from the file using `config.read(configName)`.
if os.path.exists(configName):
    try:
        config.read(configName)
    except configparser.Error as e:
        print(f"Error reading configuration file: {e}. Using default settings.")

# handling the scenario where the configuration file specified by `configName` is not found. In this case, the program prints a message indicating that the configuration file was not found and then proceeds to create a default configuration.
else:
    print(f"Configuration file '{configName}' not found. Creating a default configuration.")
    config.add_section(secTitle)
    config[secTitle]['City'] = 'New York'  # Default city
    config[secTitle]['Unit'] = 'metric'  # Default unit
    config[secTitle]['tempcheck'] = 'False'  # Default temp
    config[secTitle]['windcheck'] = 'False'  # Default wind
    config[secTitle]['timecheck'] = 'False'  # Default time
    config.read(configName)


def get_city():
    """
    The function `get_city` prompts the user to input a city name, validates the input, and asks for
    confirmation before returning the city name.

    :return: The `get_city` function is returning the city name that the user entered if it passes the
    validation checks. If the city name consists of only letters and spaces, the function will prompt
    the user to confirm if the entered city is correct. If the user confirms, the function will return
    the city name.
    """
    while True:
        city = str(input("\nPlease enter the name of the city you want to check for (e.g., 'New York').\n"))

        while not city:
            try:
                city = str(input("City name has to be a valid city.\n Please enter the name of the city you want to check for (e.g., 'New York').\n"))

            except ValueError as e:
                print(e)
                os._exit()
        if city.replace(' ', '') != '':

            if re.match(r"^[a-zA-Z\s]+$", city):  # Allows letters and spaces

                checkCity = str(input(f"\nis {city} the correct city {Yes_Or_No}\n"))
                while checkCity.lower() == 'y':
                    return city
            else:
                print("Invalid city name. Please enter only letters and spaces.")
        else:
            print("Please don't leave only spaces or blank")

def get_unit():
    """
    The function `get_unit` prompts the user to input a unit (Imperial or Metric) and allows for
    confirmation before returning the chosen unit.
    :return: The function `get_unit()` returns the unit chosen by the user (either 'Imperial' or
    'Metric').
    """
    while True:
        unit = str(input('What kind of unit would you like to use? (Imperial or Metric)\n'))

        if unit.lower() in ('imperial', 'metric'):
            checkUnit = str(input(f'\n\nis {unit} the correct unit you chose {Yes_Or_No}\n'))
            while checkUnit.lower() != 'y':
                unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
                checkUnit = str(input(f'\n\nis {unit} the correct unit you chose {Yes_Or_No}\n'))
            return unit

        else:
            print('Please enter a valid unit like (Imperial or Metric)')

def get_User_Input(UserName_input):
    """
    The function `get_User_Input` in Python prompts the user for input related to weather, time, or
    temperature, and provides assistance based on the user's query.
    
    :param UserName_input: The code snippet you provided seems to be a function that takes user input
    and processes it based on certain keywords like 'weather', 'time', 'temp', and 'help'. It then calls
    other functions like `get_city()`, `get_unit()`, and `config_Weather_Settings_()` based
    """
# First interactions along with name get_ and question asking.
    user_Query_Input = str(input(f'\nSo {UserName_input}, how can I help you?\n')).lower()
    # get_ the interaction and if the user is asking about the weather
    if 'weather' in user_Query_Input:
        city = get_city()
        unit = get_unit()
        weather_info_request = input("\nWhat about the weather would you like to know about? (e.g., temp, wind, time, sun)\n\n").lower()
        config_Weather_Settings_(city, unit, config, weather_info_request)

    # handling a specific scenario where the user's input contains the words 'time' or 'clock'. In this case, the program assumes that the user is interested in knowing the time-related information for a specific city.
    elif 'time' in user_Query_Input or 'clock' in user_Query_Input:
        city = get_city()
        config_Weather_Settings_(city, 'metric', config, 'time')

    # This part of the code is handling a specific scenario where the user's input contains the word 'temp'. When this condition is met
    elif 'temp' in user_Query_Input:
        city = get_city()
        unit = get_unit()
        config_Weather_Settings_(city, unit, config, 'temp')
    # this handles any other case other than time, temp, or weather.

    elif "help" in user_Query_Input:
        print('\nMost common responses are weather, time, and temp\n')
        get_User_Input(UserName_input)

    else:
        print("Unfortunately I can't help you with this inquiry but I can help with time or weather.")
        choice = str(input('\n\nDo you want to ask another question (Y/N)\n'))
        if choice.lower == 'y':
            get_User_Input(UserName_input)

def config_Weather_Settings_(city, unit, config, weather_info_request):
    """
    The function `config_Weather_Settings_` sets up weather settings based on user input and interacts
    with a weather service to retrieve and display weather information.
    
    :param city: The `city` parameter in the `config_Weather_Settings_` function is used to specify the
    city for which the weather settings are being configured. This parameter should be a string
    representing the name of the city for which the weather information will be retrieved
    :param unit: The `unit` parameter in the `config_Weather_Settings_` function is used to specify the
    unit of measurement for the weather data. It could be set to either 'metric' or 'imperial' depending
    on whether you want the temperature in Celsius and wind speed in meters per second (metric
    :param config: The `config_Weather_Settings_` function seems to be responsible for configuring
    weather settings based on user input. The `config` parameter likely refers to a configuration object
    or dictionary that stores settings related to the weather application
    :param weather_info_request: The `weather_info_request` parameter in the `config_Weather_Settings_` function
    is used to determine what specific weather information the user is interested in. Based on the
    user's input stored in `weather_info_request`, the function sets flags in the configuration to indicate
    whether the user is interested in temperature, wind
    """
# setting up the interactions
    
    if city == '' or unit == '':
        ValueError("Your city or unit is blank try again")
        os._exit()
    config[secTitle]['City'] = city
    config[secTitle]['Unit'] = unit

    # checking the user's input stored in the variable `weather_info_request` to determine what specific weather information the user is interested in.
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
            os._exit()
    except ConnectionError:
        ConnectionError(f"\n\nUnable to connect to the weather service. Please check your internet connection.")
    except ValueError as ve:
        ValueError(f"\n\nError: {ve}")
    except requests.exceptions.HTTPError as e:
        ConnectionError(f"\nError fetching weather data: {e}. Please check the city name or your internet connection.")
    except Exception as e:
        print(f'An unexpected error has occurred{e}')
    else:
        print('completed')

get_User_Input(UserName_input)