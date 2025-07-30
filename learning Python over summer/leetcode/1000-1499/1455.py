class Solution:
    def isPrefixOfWord( sentence: str, searchWord: str) -> int:
        # use the searchWord and find each spot that it appears in the sentence.
        # use the startswith function???
        # turn sentence into a list of strings.
        sentence = sentence.split(' ')
        print(sentence)
        for index in sentence:
            if index.startswith(searchWord):
                return sentence.index(index) +1
        return -1
sentence = "i love eating burger"
searchWord = "burg"
response = Solution.isPrefixOfWord(sentence, searchWord)
print()
print()
print()
print(response)