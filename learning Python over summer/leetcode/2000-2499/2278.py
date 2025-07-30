class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        x = s.count(letter)
        if x == 0:
            return(0)
        else:
            return (int((x / len(s) ) * 100))
        # find how many of the letters are the letter we need to find
        # divide
        # return 