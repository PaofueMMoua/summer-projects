class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        ans = 0
        count = 0
        for i in word:
            count = min(abs(ord(i) - ord(curr)), 26 - (abs(ord(curr) - ord(i))))
            ans += count + 1
            curr = i
        return(ans)