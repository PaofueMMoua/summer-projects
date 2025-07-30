class Solution:
    def arrayStringsAreEqual( word1: [str], word2: [str]) -> bool:
        # combine the word lists into a single string 
        word1String = ''
        word2String = ''
        for index in range(len(word1)):
            word1String += word1[index]
        for index in range(len(word2)):
            word2String += word2[index]
        if word1String == word2String:
            return True
        return False
        # compare the strings to see if they are equal.

        # simpler would be something like 
        
        return "".join(word1) == "".join(word2)

word1 = ["ab", "c"]
word2 = ["a", "bc"]
response = Solution.arrayStringsAreEqual(word1, word2)
print()
print()
print()
print(response)