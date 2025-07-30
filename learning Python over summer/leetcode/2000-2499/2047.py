class Solution:
    def countValidWords(sentence: str) -> int:
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        punctuation = ['.',',','?','!','-']
        count = 0
        hyphenCount = 0
        # split the sentence into a list of strings
            # use the split()
        sentenceSplit = sentence.split(' ')
        # use a for loop to loop through each instance in the sentence
        for index in sentenceSplit:
        # check if any contain a number and if they do then remove it from the list
            # use a if statement with a all() ex. all(value == x for value in sDict.values())
            if not all(values == numbers for values in index) :
            # and all(values == punctuation for values in index):            


        # check if punctuation is at the end and only the end unless its a ! by itself
            # use an all to check if there is a punctuation
            
        # check for a hyphen in the middle of any string and only in the middle of the string.
            # check for a hyphen
                if '-' in index and not index.startswith('-') and not index.endswith('-') and index.count('-') == 1 and hyphenCount != 1:
                    count += 1
                    hyphenCount = 1
                elif index == '!':
                    count += 1
                else:
                    count += 1
        return count
        # check for only one hyphen 

# sentence = "!this  1-s b8d!"
sentence = "cat and  dog"
# sentence = "alice and  bob are playing stone-game10"
response = Solution.countValidWords(sentence)
print()
print()
print()
print(response)