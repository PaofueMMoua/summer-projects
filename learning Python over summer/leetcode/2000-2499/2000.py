class Solution:
    def reversePrefix(word: str, ch: str) -> str:
        # find the first index of the character
        # get everuthing before the character to the character and save it to a new variable
        # reverse it
        # readd it back.
        chIndex = word.find(ch)
        x = word[:chIndex +1]
        word = word.removeprefix(x)
        x = x[::-1]
        word = x + word
        return word
word = "abcdefd"
ch = "d"

result = Solution.reversePrefix(word, ch)

print()
print()
print()
print()
print(result)