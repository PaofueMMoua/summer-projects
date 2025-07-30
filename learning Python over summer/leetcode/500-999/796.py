class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # check if s length is equal to goal length
        if len(s) != len(goal):
            return False
        # make a for loop that would go through the length of s
        for index in range(len(s)):
            if s == goal:
                return True
        # check if s is equal to goal
        # if it isnt then we cycle through by setting s to be equal to s[1:] + s[0]
            s = s[1:] + s[0]
        return False

s = 'abcde'
goal = 'bcdea'
response = Solution().rotateString(s, goal)

print()
print()
print(response)