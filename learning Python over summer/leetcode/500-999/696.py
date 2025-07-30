class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # set the previous current and the answers
        prev = 0
        curr = 1
        ans = 0
        # chech each instance within the range of 1 and the length of the string
        for i in range(1, len(s)):
            # if the string instance is equal to the string instance -1 then add to the current
            if s[i] == s[i - 1]:
                curr += 1
            # else add to the answer and set the previous to the current then reset the current
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1
        ans += min(prev, curr)
        return ans