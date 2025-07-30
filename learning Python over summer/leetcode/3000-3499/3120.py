class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        for c in word:
            if c.upper() in word and c.lower() in word:
                s.add(c.lower())
        return len(s)