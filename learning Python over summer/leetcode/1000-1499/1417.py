class Solution:
    def reformat( s: str) -> str:
        # make 2 lists one digits and one numbers
        # join the 2 lists together alternating.
        s = list(s)
        numList = [sub for sub in s if sub.isalpha()]
        letterList = [temp for temp in s if temp.isdigit()]
        if not numList:
            return ''
        if not letterList:
            return ''
        result =  [sub[item] for item in range(len(letterList))
            for sub in [letterList, numList]]
        result = ''.join(result)
        return result

# s = "a0b1c2"
s = 'avsd'
result = Solution.reformat(s)
print()
print()
print()
print(result)