class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # seperate the string fully
        result = [''] * len(s)
        # make a for loop that is going to get the index and the character of s 
        for index, char in enumerate(s):
            # 
            result[indices[index]] = char
        return "".join(result)