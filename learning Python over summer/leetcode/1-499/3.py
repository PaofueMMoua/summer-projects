class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
# get the string.
# find a substring.
    # potentially use the find function
# check if the length is equal to 0 or not.
    # if it is equal to 0 then return 
# check for duplicate characters.
# output the length of the final substring.
        seen = set()
        # use a set() to get the string and split it up
        left = 0
        # set a variable to 0 to let it be the left 
        max_len = 0
        # max length

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

s = "abcabcbb"
result = Solution.lengthOfLongestSubstring(s)

print()
print()
print()
print()
print(result)