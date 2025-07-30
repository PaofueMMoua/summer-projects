class Solution:
    def checkRecord(self, s: str) -> bool:
        # check if the string contains 3 l's in a row then return False
        if 'LLL' in s or s.count('A' >= 2):
            return False
        return True
        # return true otherwise.

s = 'PPALLAP'
response = Solution().checkRecord(s)

print()
print()
print(response)