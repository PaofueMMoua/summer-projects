class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # find the word after the other words.
        # just find the after
        words = text.split(" ")
        result = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
        return result