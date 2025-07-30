class Solution:
    def secondHighest( s: str) -> int:
        

# get s
# get all digits
# get the second larges
    # for loop to go through each digit beginning with the largest digit and finding the next largest one.
        digits = ''.join(filter(str.isdigit, s))
        if digits == '':
            return -1
        print(str(int(max(digits)) -1))
        if str(int(max(digits)) -1) in s:
            return int(max(digits)) -1
        elif str(int(max(digits)) -1) not in s and digits.replace(max(digits), '') != '':
            digits = digits.replace(max(digits), '')
            return int(max(digits))
        print(str(int(max(digits)) -1))
        return -1


# 
# 
s = "abc1111"
a = Solution.secondHighest(s)
print()
print()
print()
print(a)
print()
print()
print()