class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # check if s contains all the same letters as t
        # use a for loop to see if each letter of s is in t
        if len(t) > len(s):
            return False
        for character in s:
            if s.count(character) != t.count(character):
                return False
        return True


s = 'anagram'
t = 'margana'
response = Solution().isAnagram(s,t)

print()
print()
print(response)