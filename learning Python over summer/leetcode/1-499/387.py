# class Solution:
#     def firstUniqChar(self, s: str) -> int:
s = "leetcode"
        # use the find function or the index function to find the letters
for charIndex in s:
    if s.rindex(charIndex) == s.index(charIndex):
                # return s.index[charIndex]
        print(s.index(charIndex))
return(-1)
                # return -1



# response = Solution.firstUniqChar(s)
