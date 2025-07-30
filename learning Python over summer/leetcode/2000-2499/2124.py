class Solution:
    def checkString( s: str) -> bool:
        # for letter in range(len(s)):
        #     if letter == len(s):
        #         break
        #     if s[letter] == 'b' and s[letter +1] == 'a':
        #         return False
        # return True
        return 'ba' not in s

s = "aaabbb"
a = Solution.checkString(s)

print()
print()
print()
print(a)
print()
print()
print()