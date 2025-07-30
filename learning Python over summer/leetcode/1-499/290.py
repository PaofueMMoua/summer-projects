# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
class Solution:
    def wordPattern( pattern: str, s: str) -> bool:
        
        # split the s
        s = s.split(' ')
        # check if not the len(s) is equal to the len( pattern) then returning False
        if  not len(s) == len(pattern):
                return False
        # return true if the length of the set of zipping the pattern and s  is equal to the length of the set s and is equal to the length of the set pattern.
        return len(set(zip(pattern, s))) == len(set(s)) == len(set(pattern))

        # compare if the pattern matches up with the s
pattern = "abba"
s = "dog cat cat dog"

response = Solution.wordPattern(pattern, s)
print()
print()
print()
print(response)