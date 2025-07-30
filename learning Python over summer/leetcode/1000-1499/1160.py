class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # loop through each nstance of words
        # results = 0
        # for word in words:
        #     for char in word:
        #         if char not in chars or chars.count(char) < word.count(char):
        #             break
        #         else: 
        #             results += len(word)
        # return results
        # if the word characters are equal to the characters avaluable or is less than.
        # have a temp that is the results
        
        res = 0
        for word in words:
            for c in word:
                if c not in chars or chars.count(c) < word.count(c):
                    break
            else:
                res +=len(word)
        return res