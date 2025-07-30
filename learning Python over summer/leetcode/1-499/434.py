class Solution:
    def countSegments(self, s: str) -> int:
# getting the segments
# setting the segments into an list
# split() ?
        s = "A man, a plan, a canal Panama"
        stringList = []
        stringList += s.split()
        print(stringList)
        return(len(stringList))
# 


s = "A man, a plan, a canal Panama"
# s = "race a car"
# s = "racecar"
# s = " "
response = Solution().countSegments(s)

print(response)