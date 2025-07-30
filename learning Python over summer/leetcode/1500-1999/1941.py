class Solution:
    def areOccurrencesEqual( s: str) -> bool:
        # convert s to a dictionary that adds one to each 
        sDict = {}
        x = 0
        for character in s:
            sDict.setdefault(character, 0)
            sDict[character] += 1
            x = sDict[character]
        # check all values to see if they are equal or not.
        return(all(value == x for value in sDict.values()))

s = "abacbc"
response = Solution.areOccurrencesEqual(s)
print()
print()
print()
print(response)