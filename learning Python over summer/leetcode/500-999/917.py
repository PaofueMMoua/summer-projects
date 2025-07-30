class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # find all letters 
        letters = [char for char in s if char.isalpha()]
        # reverse letters
        letters.reverse()
        # iterate through the letters
        letterInteration = iter(letters)
        # find the placements of non letters
        # get the letters out of the string 
        # replace the temp for the letters.
        return(''.join(next(letterInteration) if char.isalpha() else char for char in s))

        # Extract all letters and reverse them
        # letters = [char for char in s if char.isalpha()]
        # letters.reverse()
        
        # # Iterator for the reversed letters
        # letter_iter = iter(letters)
        
        # # Rebuild the string with letters replaced
        # result = ''.join(next(letter_iter) if char.isalpha() else char for char in s)
        
        # return result  
s = "ab-cd"
response = Solution().reverseOnlyLetters(s)
print()
print()
print()
print(response)