import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

# remove all spaces and symbols.
        
        s2 = re.sub('[^A-Za-z0-9]+', '', s).lower()
        s = s2
        # for i in range(len(s)):
        #     if s[i].isalpha == False:
        #         s = s.replace(s[i], ' ')
        #         print(s)
    # set another variable to it backwards?
        sBackwards = s[::-1]
        
     # compare both using their index
        if s == sBackwards:
            return True
        else:
            return False
      # if they dont match 100% then retun False
       # if they do match return True





s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = "racecar"
# s = " "
response = Solution().isPalindrome(s)
