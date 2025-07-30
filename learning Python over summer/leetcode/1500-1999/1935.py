class Solution:
    def canBeTypedWords( text: str, brokenLetters: str) -> int:
# change text into a list
        text = text.split(' ')
        count = 0
        brokenLetters = list(brokenLetters)
# use a for loop to cycle through each instance within the text list. 
        for index in range(len(text)):
            if not any(value in brokenLetters for value in text[index]):
                count += 1
        return(count)
        
# check if it contains anythin within the broken letters.

text = "hello world"
brokenLetters = "ad"

response = Solution.canBeTypedWords(text, brokenLetters)
print()
print()
print()
print(response)