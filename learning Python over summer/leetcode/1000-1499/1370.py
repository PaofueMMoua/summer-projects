class Solution:
    def sortString(self, s: str) -> str:
        # set the list
        s = list(s)
        # make a random variable
        result = ''
        # make a while loop that loops through s
        # loop through each letter in a sorted set of s  and then remove the letter and then add letter to the result.
        while s:
            for letter in sorted(set(s)):
                s.remove(letter)
                result += letter
            for letter in sorted(set(s), reverse=True):
                s.remove(letter)
                result += letter
        return result