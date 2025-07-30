class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # d means decrease slowly from the max index
        # i means increase from 0
        # make a for loop that loops through the length of the string
        # makee the variables d and i change depending on what appears in the loop. 
        # the loop could gothrough each character witihin the Loop.
        answ = []
        d = len(s)
        i = 0
        for character in s :
            if character == 'D':
                answ.append(d)
                d -= 1
            if character == 'I':
                answ.append(i)
                i += 1
        answ.append(d)
        return answ
