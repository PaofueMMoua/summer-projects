# for character in magazine:
#             magazineCharCount.setdefault(character, 0)
#             magazineCharCount[character] += 1
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        # make a dicitionary and have every word from the paragraph put into the dictionary and how many times it is in there.
        paragraphDictionary = {}
        paragraph = paragraph.replace('!', '').replace('?', '').replace("'", '').replace(',', '').replace(';', '').replace('.', '')
        paragraph = paragraph.lower()
        paragraphtemp = paragraph.split(' ')
        
        for word in paragraphtemp:
            paragraphDictionary.setdefault(word,0)
            paragraphDictionary[word] += 1
        print(paragraphDictionary)
        for word in banned:
            paragraphDictionary[word] = 0
        print(paragraphDictionary)
        temporaryGreatest = 0
        temporaryKey = ''
        for key in paragraphDictionary:
            if paragraphDictionary.get(key) > temporaryGreatest:
                temporaryGreatest = paragraphDictionary.get(key)
                temporaryKey = key
        return temporaryKey
        # return the word with the biggest value.
        # make a for loop to find the word with the biggest value


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
response = Solution().mostCommonWord(paragraph, banned)

print()
print()
print(response)