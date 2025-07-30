class Solution:
    def prefixCount( words: [str], pref: str) -> int:
        # get the words
        # check if the words contain the prefix
        # use the if all
        # ex. return(all(value == x for value in sDict.values()))
        count = 0
        for word in words:
                if word.startswith(pref):
                    count += 1
        return count

words = ["pay","attention","practice","attend"]
pref = "at"
response = Solution.prefixCount(words, pref)
print()
print()
print()
print(response)