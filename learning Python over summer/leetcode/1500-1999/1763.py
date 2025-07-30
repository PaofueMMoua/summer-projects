class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # checking if it contains a uppercase for each lower case and so on.
        # get the largest subsequence that works.
        # if there are none nice substrings then return 