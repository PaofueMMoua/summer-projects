class Solution:
    def mergeAlternately( word1: str, word2: str) -> str:
        # merge the strings together while alternating.
        # 

        result = []
        for i , j in zip(word1,word2):
            result.append(i)
            result.append(j)
        result.append(word1[len(word2):])
        result.append(word2[len(word1):])
        return "".join(result)
word1 = "abc"
word2 = "pqr"
response = Solution.mergeAlternately(word1, word2)
print()
print()
print()
print(response)