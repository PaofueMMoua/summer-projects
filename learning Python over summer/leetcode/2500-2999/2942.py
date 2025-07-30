class Solution:
    def findWordsContaining( words: list[str], x: str) -> [int]:
        # search if the word in words contains a substring of x.
        # 
        tempList = []
        for word in range(len(words)):
            if x in words[word]:
                tempList.append(word)
        return tempList

words = ["leet","code"]
x = "e"
# response = Solution().findWordsContaining(words, x)

print()
print()
print(Solution().findWordsContaining(words))