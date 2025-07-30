class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # make a for loop to loop through each character of a 
        # check if character of a is equal to the character of b
        if b not in a or a not in b:
            return max(len(b),len(a))
        return -1  


a = 'aba'
b = 'cdc'

response = Solution().findLUSlength(a, b)

print()
print()
print(response)