year = input()
x = 365
# you can use f and then {} to format other things like ints or others into string and then into the statement without having to use the "+ year +" 
yearString = f'The year is {year}'

if int(year) % 4 == 0:
    x = x + 1
    # if its a leap year this is adding on the fact that its a leap year to the string.
    yearString += ' this is a leap year'
    
# adding a period afterwards to make the string more simpler.
yearString += '.'
print(yearString)
# printing out the days that are within the leap year.
print (f'There are {x} days in the year')

