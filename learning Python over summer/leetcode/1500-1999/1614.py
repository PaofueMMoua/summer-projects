class Solution:
    def maxDepth( s: str) -> int:
        perenthesisMinusAll = ''
# set a string or something to be the perenthesis after number and other removal
        maxLen = 0
        tempLen = 0

# get the perenthesis 
        for everything in range(len(s)):
            if s[everything] == '(' or s[everything] == ')':
                perenthesisMinusAll += s[everything]
    # put the perenthesis into the order that they showup in
        for perenLen in range(len(perenthesisMinusAll)):
            if perenthesisMinusAll[perenLen] == perenthesisMinusAll[perenLen -1] :
                tempLen += 1
            else:
                tempLen = 0
            if tempLen > maxLen:
                maxLen += tempLen
        return maxLen
    # find the most of the same perenthesis side in a row.

s = "(1+(2*3)+((8)/4))+1"
print()
print()
print()
print(Solution.maxDepth(s))
print()
print()
print()