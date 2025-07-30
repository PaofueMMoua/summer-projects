import WeatherApp2
import configparser

configName = 'weatherConfig.ini'
sectionTitle = 'CityInfo'

UserName_input = str(input('Hello, whats your name\n'))
user_Query_Input = str(input(f'So {UserName_input}, how can I help you?\n'))
# user_Query_Input = 'weather'

def gettingUserInput(UserName_input, user_Query_Input):
# First interactions along with name getting and question asking.

    # getting the interaction and if the user is asking about the weather
    if user_Query_Input.lower().find('weather') != -1 :
        config = configparser.ConfigParser()
        config.read(configName)
        
    # setting the city and the unit to the config file
        city = str(input('What city would you like to know the weather for?\n'))
        checkCity = str(input(f"\n\nis {city} the correct city Y / N\n"))
        while checkCity.lower() != 'y':
            city = str(input('What city would you like to know the weather for?\n'))
            checkCity = str(input(f"\n\nis {city} the correct city Y / N\n"))
            print(checkCity.lower() != 'y')

        unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
        checkUnit = str(input(f'\n\nis {unit} the correct unit you chose Y / N\n'))
        while checkUnit.lower() != 'y':
            unit = str(input('What kind of unit would you like to use? Imperial or Metric?\n'))
            checkUnit = str(input(f'\n\nis {unit} the correct unit you chose Y / N\n'))

        thirdInteraction = str(input('What about the weather would you like to know about?\n'))
        config_Weather_Settings_(city, unit, config, thirdInteraction)
    else:
        print("Unfortunately I can't help you with this inquiry")

def config_Weather_Settings_(city, unit, config, thirdInteraction):
# setting up the interactions
    config['CityInfo']['City'] = city
    config['CityInfo']['Unit'] = unit

    
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

gettingUserInput(UserName_input, user_Query_Input)

# getting the interaction if it isn't talking about the weather.