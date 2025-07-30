class Solution:
    def isPrefixString( s: str, words: [str]) -> bool:
        # add the words together without any space and then check if s is the prefix.
        words = ''.join(words)
        if words.startswith(s):
            return True
        return False
            

# sentence = sentence.split(' ')
#         print(sentence)
#         for index in sentence:
#             if index.startswith(searchWord):
#                 return sentence.index(index) +1
#         return -1

s = "ccccccccc"
words = ["c","cc"]

response = Solution.isPrefixString(s, words)
print()
print()
print()
print(response)