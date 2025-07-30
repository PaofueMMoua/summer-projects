# using the 24 hour clock checking what the time is and along with that getting the target hours.

yourtime = input("What is the time 'in hours'")
targetHours = input('what is your target hours to wait')

alarmText = "You will have to wait"

# this is to get the total time that you need to wait plus the time that it is currently.
totalWaitTime = int(yourtime) + int(targetHours)
alarmTime = totalWaitTime % 24
alarmDays = totalWaitTime // 24

# Checking if the alarmDays variable is not equal to 0
if alarmDays != 0:
    # updating the alarmText to be equal to itself adding on the days and the words 'days and'
    alarmText += f'{alarmText} {alarmDays} days and '
    
    # printing the alarmText with the time and then hours. at the end.
print(f'{alarmText}{alarmTime} hours.')