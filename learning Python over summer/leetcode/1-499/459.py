class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
    # TODO: get s
    # TODO: get a substring of s
        # TODO: getting a good substring of s
            # TODO: slicing?
        #subString = s in (s+s) [1:-1]
        substring = s+s
        if s in substring [1:-1]:
            return True
        return False
        #print((s+s) [1:-1])
    # TODO: check if the substring repeats
        # TODO: return true
    # TODO: return False

s = 'abab'
result = Solution.repeatedSubstringPattern(s, s)

print()
print()
print()
print()
print(result)