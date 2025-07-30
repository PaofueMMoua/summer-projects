# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
word = 'USA'
# word = 'Google'
# word = 'leetcode'
# word = 'LeetCode'
# TODO: detecting capital properly

# TODO: given a word return true if the capitalization is used correctly else return false
# TODO: set a temporary word so you can change the word
changingWord = word
# TODO: take the word and check if its all lower case return true
if changingWord.lower() == word:
    return True
# TODO: check if everything but the first letter is capital using the index [1:]
elif (changingWord[0] + changingWord[1:].lower()) == word:
    return True
# TODO: check if everything is capital
elif changingWord.upper() == word:
    return True
else:
    return False