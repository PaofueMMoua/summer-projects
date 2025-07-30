import numpy as np
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        count = 0
        for i in range(len(words)):
            words[i] = ''.join([morse[ord(j) - ord('a')] for j in words[i]])
        if len(words) == 1:
            return 1
        else:
            for i in np.unique(words):
                count = count +1
            return count