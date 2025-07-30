class Solution:
    def maxPower(self, s: str) -> int:

        lst = 0
        temp = 'ab'
        c = 1
        for i in s:
            if i != temp:
                temp = i
                lst = max(lst, c)
                c = 1
            else:
                c += 1
        lst = max(lst, c)
        return lst