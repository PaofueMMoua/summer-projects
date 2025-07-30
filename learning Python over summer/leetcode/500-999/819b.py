class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        split_chars = r"[ !?',;.]"
        words = [word.lower() for word in re.split(split_chars, paragraph) if word and word.lower() not in banned]
        w_dict = {}
        for w in words:
            if w not in w_dict:
                w_dict[w] = 0
            w_dict[w] += 1
        max_so_far = 0
        max_word = ""
        for k, v in w_dict.items():
            if v > max_so_far:
                max_so_far = v
                max_word = k
        return max_word