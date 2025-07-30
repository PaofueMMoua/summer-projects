class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s = s[0:k]
        s = ' '.join(s)
        return s