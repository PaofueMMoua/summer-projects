from collections import Counter
class Solution:
    def checkAlmostEquivalent( word1: str, word2: str) -> bool:
        

# make a dictionary to count the amount of times that each letter appears in word1 and word 2
    # can use counter from collections

        # wordDict1 = {}
        # splitWord1 = word1.split('')
        # for letter in splitWord1:
        #     wordDict1.setdefault(letter,0)
        #     wordDict1[letter] += 1
        # print(wordDict1)

        wordCounting = Counter(word1)
        wordCountingTwo = Counter(word2)
        print(wordCounting)
        print(wordCountingTwo)

        for key in wordCounting:
            if wordCounting.get(key) not in wordCountingTwo:
                wordCountingTwo.setdefault(key, 0)
            if abs(wordCounting.get(key) - wordCountingTwo.get(key)) > 3:
                return False
        return True

        # temporaryGreatest = 0
            # setting a temp greatest
        # temporaryKey = ''
            # setting a temp key
        # for key in paragraphDictionary:
            # a for loop to find the key in the paragraph dictionary
        #     if paragraphDictionary.get(key) > temporaryGreatest:
            # 
        #         temporaryGreatest = paragraphDictionary.get(key)
        #         temporaryKey = key
        # return temporaryKey
    
# compare the two using the letters. and a for loop?
        # for i in range(len(wordCounting)):
        #     if wordCounting[i]
# compare the letters by seeing how many there are and the difference between how many there are
# if any is more than 3 differences in any letter then return with False 
# else return true
word1 = "aaaa"
word2 = "baaaccb"
response = Solution.checkAlmostEquivalent(word1, word2)
print()
print()
print()
print(response)
print()
print()
print()

# Example 2:

# Input: word1 = "abcdeef", word2 = "abaaacc"
# Output: true
# Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
# - 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
# - 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
# - 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
# - 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
# - 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
# - 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.


# words = set(word1 + word2)
#         for w in words:
#             if abs(word1.count(w) - word2.count(w)) >3:
#                 return False
#         return True