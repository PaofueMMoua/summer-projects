class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
# combine both sentences with a space seperating them
        s3 = s1 + ' ' + s2
# split through spaces
        s4 = s3
        s3 = s3.split(' ')
        for index in range(len(s3)):
            if s3.count(s3[index]) > 1:
                s4 = s4.replace(' '+s3[index]+' ', '   ')
        s4 = s4.split()
        print(s3)
        return(s4)
# check if the word repeats and if it does then replace both instances with a ' '
# return the remaning words

s1 = "d b zu d t"
s2 = "udb zu ap"

response = Solution().uncommonFromSentences(s1, s2)

print()
print()
print(response)