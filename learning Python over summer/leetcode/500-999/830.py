class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # split the string into a lsit that seperated the different letter sections together
        # make a for loop that is going to cucle through each index of the list and then retrun the count of characters within. 
        # with the returned number cehck if it is greater than 3 and return true and the index of it if so.
        
        # set variables like the result and a int so we can get the start variable
        result = []
        start = 0
        while start < len(s):
            end = start
            while end < len(s) and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                result.append([start, end - 1])
            start = end
        return result
        # loop through the string to find any groups
        # while loop to make another variable move further untill it hits a letter that is different than what is expected.
        # if its greater than 3 then return it to a list