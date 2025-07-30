class Solution:
    def largestOddNumber(num: str) -> str:
        # return the largest odd number?
        # if it is odd number then return the number 
        i = len(num)-1
        for i in range(i,-1,-1):
            if int(num[i])%2 == 1:
                return num[:i+1]
        return ""
        # if it is a even number find the largest odd number

num = '1231232'
response = Solution.largestOddNumber(num)
print()
print()
print()
print(response)