class Solution:
    def numOfStrings(patterns: [str], word: str) -> int:
        count = 0
        for iteration in patterns:
            if iteration in word:
                count += 1
                print(iteration)
        return count

# sentence = sentence.split(' ')
#         print(sentence)
#         for index in sentence:
#             if index.startswith(searchWord):
#                 return sentence.index(index) +1
#         return -1

patterns = ["a","abc","bc","d"]
word = "abc"
response = Solution.numOfStrings(patterns, word)
print()
print()
print()
print(response)