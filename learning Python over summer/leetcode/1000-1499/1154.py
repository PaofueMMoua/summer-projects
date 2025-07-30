class Solution:
    def dayOfYear(date: str) -> int:
        # if the year isnt a leap year then set month days accordingly.
        months = [0, 31, 59 ,90, 120, 151, 181, 212, 243, 273, 304, 334]
        # split the date by the - 
        date = date.split('-')
        print(date)

        daysIntoYear = 0

        # if the year is a leap year then set month days accordingly.
        if int(date[0]) % 4 == 0:
            if (int(date[0]) % 100) == 0 and (int(date[0]) % 400) != 0:
                months = [0, 31, 59 ,90, 120, 151, 181, 212, 243, 273, 304, 334]
            else:
                months = [0, 31, 60 ,91, 121, 152, 182, 213, 244, 274, 305, 335]
        # check the months now
        for days in range(len(months)):
            if int(date[1]) == days + 1:
                daysIntoYear += months[days]
                break
        daysIntoYear += int(date[2])
        print(int(date[0]))
        return(daysIntoYear)



date = "1900-05-02"
response = Solution.dayOfYear(date)
print()
print()
print()
print(response)