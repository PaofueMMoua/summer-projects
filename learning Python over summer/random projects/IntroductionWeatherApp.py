import WeatherApp2
import configparser

configName = 'weatherConfig.ini'
sectionTitle = 'CityInfo'

UserName_input = str(input('\nHello, whats your name\n')).capitalize()

config = configparser.ConfigParser()
config.read(configName)

def getting_city():
    city = str(input("Please enter the name of the city you want to check for (e.g., 'New York').\n"))
    while city.replace(' ', '') == '':
        city = str(input("Please enter the name of the city you want to check for (e.g., 'New York').\n"))
    checkCity = str(input(f"\n\nis {city} the correct city Y / N\n"))
    while checkCity.lower() != 'y':
        city = str(input('What city would you like to know the weather for?\n'))
        checkCity = str(input(f"\n\nis {city} the correct city Y / N\n"))
    return city

def getting_unit():
    unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
    checkUnit = str(input(f'\n\nis {unit} the correct unit you chose Y / N\n'))
    while checkUnit.lower() != 'y':
        unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
        checkUnit = str(input(f'\n\nis {unit} the correct unit you chose Y / N\n'))
    return unit

def getting_User_Input(UserName_input):
# First interactions along with name getting_ and question asking.
    user_Query_Input = str(input(f'\nSo {UserName_input}, how can I help you?\n'))
    # getting_ the interaction and if the user is asking about the weather
    if user_Query_Input.lower().find('weather') != -1 :

    # setting the city and the unit to the config file and validation for what city and unit
        # getting_ user input for the city they want to check the weather for, validating the input, and confirming if the city entered is correct.
        city = getting_city()

        #  responsible for getting_ user input regarding the preferred unit of measurement for weather data.
        unit = getting_unit()

        thirdInteraction = input("\nWhat about the weather would you like to know about? (e.g., temp, wind, time, sun)\n\n").lower()
        config_Weather_Settings_(city, unit, config, thirdInteraction)
        
    # handling a specific scenario where the user's input contains the words 'time' or 'clock'. In this case, the program assumes that the user is interested in knowing the time-related information for a specific city.
    elif user_Query_Input.lower().find('time') != -1 or user_Query_Input.lower().find('clock') != -1:
        city = getting_city()
        unit = 'metric'
        thirdInteraction = 'time'
        config_Weather_Settings_(city, unit, config, thirdInteraction)

    # This part of the code is handling a specific scenario where the user's input contains the word 'temp'. When this condition is met
    elif user_Query_Input.lower().find('temp') != -1:
        city = getting_city()
        unit = getting_unit()
        thirdInteraction = 'temp'
        config_Weather_Settings_(city, unit, config, thirdInteraction)
    # this handles any other case other than time, temp, or weather.
    
    elif user_Query_Input.lower().find('help') != -1:
        print('\nMost common responses are weather, time, and temp\n')
        getting_User_Input(UserName_input)
    else:
        print("Unfortunately I can't help you with this inquiry but I can help with time or weather.")
        choice = str(input('\n\nDo you want to ask another question Y/N\n'))
        if choice.lower == 'y':
            getting_User_Input(UserName_input)

def config_Weather_Settings_(city, unit, config, thirdInteraction):
# setting up the interactions
    config['CityInfo']['City'] = city
    config['CityInfo']['Unit'] = unit

    # checking the user's input stored in the variable `thirdInteraction` to determine what specific weather information the user is interested in.
    if thirdInteraction.lower().find('temp') != -1:
        config['CityInfo']['tempcheck'] = 'True'
    else:
        config['CityInfo']['tempcheck'] = 'False'

    if thirdInteraction.lower().find('weather') != -1 or thirdInteraction.lower().find('wind') != -1 :
        config['CityInfo']['windcheck'] = 'True'
    else:
        config['CityInfo']['windcheck'] = 'False'

    if thirdInteraction.lower().find('time') != -1 or thirdInteraction.lower().find('sun') != -1:
        config['CityInfo']['timecheck'] = 'True'
    else:
        config['CityInfo']['timecheck'] = 'False'

    with open(configName, 'w') as configfile:
        config.write(configfile)

    try:
        temp = WeatherApp2.Weather(config, sectionTitle)
        print(temp.run())
    except:
        raise ValueError("\n\n The weather data couldn't be found at this time please try again later.\n")

getting_User_Input(UserName_input)