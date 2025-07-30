class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.split(' ')
        s.strip()
        s = len(s)
        return(s)


# s = "Hello"
# s = "Hello World"
s = "Hello World Snuggie "
# s = "Hello World Snuggie Is"
# s = "Hello World Snuggie Is Not "
# s = "Hello World Snuggie Is Not Cool"

response = Solution().lengthOfLastWord(s)


print()
print()
print(response)