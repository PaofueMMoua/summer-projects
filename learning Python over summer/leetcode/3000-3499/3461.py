class Solution:
    def hasSameDigits( s: str) -> bool:
        ending = ''
        # make a for loop to loop through s 
        for i in range(len(s)) :
                if i != len(s) - 1 :
                    ending += str((int(s[i]) + int(s[i+1])) % 10)
        return ending
        # (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
        # save the end to a new string
        # return the new string.

s = "3902"
a = Solution.hasSameDigits(s)
print()
print()
print(a)
print()
print()
