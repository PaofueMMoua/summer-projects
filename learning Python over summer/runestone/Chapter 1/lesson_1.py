import datetime

print('Hello, world!')
# asking the  name of the person who is running the program.
print('What is your name?')
# setting myName to be equal to whatever the person inputs.
myName = input()
# setting the program to output the person's name within a statement.
print('It is good to meet you, ' + myName)
print('The length of your name is:')
# getting the length of the name through using the len function that checks the amount of characters within a string.
print(len(myName))
print('What is your age?')
# setting myAge to equal to the input
myAge = input()        
print('You will be ' + str(int(myAge) + 1) + ' in a year.')        
