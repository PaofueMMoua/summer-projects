from collections import Counter

class Solution:
    def shortestCompletingWord(self,  licensePlate: str, words: [str]) -> str:
        # turn license plate into a list
        wordsMatchLetters = 0
        mainWord = ''
        licensePlate = [i for i in licensePlate.lower() if i.isalpha()]
        print(licensePlate)
        wordCounter1 = Counter(licensePlate)
        # loop through words
        for word in words:
            wordCounter2 = Counter(word)
            wordsTotalCount = wordCounter1 & wordCounter2
            wordsTotalCount = wordsTotalCount.total()
            if wordsTotalCount > wordsMatchLetters:
                wordsMatchLetters = wordsTotalCount
                mainWord = word
        return mainWord
    
    # class Solution:
    # def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # t = [i for i in licensePlate.lower() if i.isalpha()]
        # l = float('inf')
        # r = ''
        # for i in words:
        #     if Counter(i) & Counter(t) == Counter(t) and len(i) < l:
        #         l = len(i)
        #         r = i
        # return r
                
        # check if each index of words contains a letter of license plate and how many.
        # if it sets a new record then it becomes the main word and sets the main word letter checking count and so on.


licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
response = Solution().shortestCompletingWord(licensePlate, words)

print()
print()
print(response)