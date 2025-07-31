import WeatherApp2
import configparser


configName = 'weatherConfig.ini'
secTitle = 'CityInfo'

UserName_input = str(input('\nHello, whats your name\n')).capitalize()
Yes_Or_No = '(Y / N)'

config = configparser.ConfigParser()
config.read(configName)

def get_city():
    while True:
        city = str(input("Please enter the name of the city you want to check for (e.g., 'New York').\n"))
        while not city:
            city = str(input("City name has to be a valid city.\n Please enter the name of the city you want to check for (e.g., 'New York').\n"))
        checkCity = str(input(f"\n\nis {city} the correct city {Yes_Or_No}\n"))
        while checkCity.lower() == 'y':
            return city

def get_unit():
    while True:
        unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
        if unit.lower() in ('imperial', 'metric'):
            checkUnit = str(input(f'\n\nis {unit} the correct unit you chose {Yes_Or_No}\n'))
            while checkUnit.lower() != 'y':
                unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
                checkUnit = str(input(f'\n\nis {unit} the correct unit you chose {Yes_Or_No}\n'))
            return unit
        else:
            print('Please enter a valid unit')

def get_User_Input(UserName_input):
# First interactions along with name get_ and question asking.
    user_Query_Input = str(input(f'\nSo {UserName_input}, how can I help you?\n')).lower()
    # get_ the interaction and if the user is asking about the weather
    if 'weather' in user_Query_Input:
        city = get_city()
        unit = get_unit()
        thirdInteraction = input("\nWhat about the weather would you like to know about? (e.g., temp, wind, time, sun)\n\n").lower()
        config_Weather_Settings_(city, unit, config, thirdInteraction)
    # handling a specific scenario where the user's input contains the words 'time' or 'clock'. In this case, the program assumes that the user is interested in knowing the time-related information for a specific city.
    elif 'time' in user_Query_Input or 'clock' in user_Query_Input:
        city = get_city()
        unit = 'metric'
        thirdInteraction = 'time'
        config_Weather_Settings_(city, unit, config, 'time')

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

def config_Weather_Settings_(city, unit, config, thirdInteraction):
# setting up the interactions

    config[secTitle]['City'] = city
    config[secTitle]['Unit'] = unit

    # checking the user's input stored in the variable `thirdInteraction` to determine what specific weather information the user is interested in.
    config[secTitle]['tempcheck'] = 'True' if 'temp' in thirdInteraction else 'False'
    config[secTitle]['windcheck'] = 'True' if 'weather' in thirdInteraction or 'wind' in thirdInteraction else 'False'
    config[secTitle]['timecheck'] = 'True' if 'time' in thirdInteraction or 'sun' in thirdInteraction else 'False'

    with open(configName, 'w') as configfile:
        config.write(configfile)

    try:
        temp = WeatherApp2.Weather(config, secTitle)
        print(temp.run())
    except:
        raise ValueError(f"\n\n Unfortunately I couldn't get the information from the server.\n \n Just to check you put in {city} and {unit}.\n")

get_User_Input(UserName_input)