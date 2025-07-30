class Solution:
    def isValid( word: str) -> bool:

# requirements
    # It contains a minimum of 3 characters.
    # It contains only digits (0-9), and English letters (uppercase and lowercase).
    # It includes at least one vowel.
    # It includes at least one consonant.
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']


# get the word
# check if the word contains all of the requirements.
        if any(substring in word for substring in vowels) and len(word) >= 3 and any(substring in word for substring in consonant) and word.isalnum:
            return True
        return False
    # if the word is a minimum of 3 characters and contains only digits and english letters and contains at least one vowel and contains at least one constonant
# return true if it contains all of the requirements
# return False otherwise.
word = "234Adas"
a = Solution.isValid(word)
print()
print()
print()
print(a)
print()
print()
print()