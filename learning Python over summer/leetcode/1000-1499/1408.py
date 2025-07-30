class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # make a list.
        found = []
        # make a for loop thaet is going to loop through each index of words.
        for word in words:
        # if any word is found in another word then add it to the list.
            if any(word in y and word != y for y in words):
                found.append(word)
        return found