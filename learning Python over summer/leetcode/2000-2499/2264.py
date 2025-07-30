class Solution:
    def largestGoodInteger( num: str) -> str:
        number = ["000","111","222","333","444","555","666","777","888","999"]
        highestNum = ''
        for numbers in number:
            if numbers in num:
                highestNum = numbers
        return highestNum
            


num = "6777133339"
print()
print(Solution.largestGoodInteger(num))
print()