class Solution:
    def reorderSpaces(text: str) -> str:
        # finding the total amount of spaces.
        spaceAmount = text.count(' ')
        # finding the amount of words.
        temp = text.split()
        wordAmount = len(temp)
        print(spaceAmount)
        print(wordAmount)

        # divide the amount of spaces by the amount of words
        if spaceAmount > 0:
            if wordAmount > 1:
                spaceIncrement = spaceAmount // (wordAmount - 1)
                spaceRemaning = spaceAmount % (wordAmount - 1)
                temp = (' '*spaceIncrement).join(temp)
                temp += ' '*spaceRemaning
            else:
                temp = ''.join(temp)
                temp += ' '*spaceAmount
        else:
            temp = ''.join(temp)
        print(temp)
        return temp
        # if there are any remainders then itll go that many times at the end of the string.

text = "  this   is  a sentence "
result = Solution.reorderSpaces(text)
print()
print()
print()
print(result)