class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # while loop to loop through each character in the first word
        # check whether the index of the first word is in the other words. using a for loop to see all the other words.
        # have a if statement check if they contain it or not and if they do then remove the letter
        minimum_freq = Counter(words[0])
        for word in words:
            minimum_freq &= Counter(word)
        return list(minimum_freq.elements())
    
words = ["bella","label","roller"]

response = Solution.commonChars(words)
print()
print()
print()
print(response)