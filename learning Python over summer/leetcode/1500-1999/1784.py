class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # check if there is a substring of 11 and if there is then return true.
        sub = '11'
        if '11' in s:
            return True
        return False