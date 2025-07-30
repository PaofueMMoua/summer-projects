class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
# check the length of each minus the backspace
# get the length of each
# get the backspace amount of each
# remove the backspace amount * 2 from each. using count?
        for index in range(len(s)):
            if s[index] == '#':
                s = s[:index -1] + '  ' + s[index + 1:]
        for index in range(len(t)):
            if t[index] == '#':
                t = t[:index -1] + '  ' + t[index + 1:]
        print(s)
        print(t)
        if s == t:
            return True 
        return False
# see if the lengths are equal to eachother 

s = "a#b#c#"
t = "a#b#c#"
response = Solution().backspaceCompare(s, t)

print()
print()
print(response)