class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # make a dictionary?
        # make a for loop that will cycle through the enumerate order.
        # make a for loop that loops through each index in the length of words
        hashmap = {}
        for i, c in enumerate(order):
            hashmap[c] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if hashmap[word1[j]] > hashmap[word2[j]]:
                        return False
                    break
        return True