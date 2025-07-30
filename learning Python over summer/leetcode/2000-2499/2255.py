class Solution:
    def countPrefixes( words: [str], s: str) -> int:
        # check if all instances of words are in s
        # if they are then add one to count.
        count = 0
        for word in words:
                if s.startswith(word):
                    count += 1
        return count
words = ["a","b","c","ab","bc","abc"]
s = "abc"
response = Solution.countPrefixes(words, s)
print()
print()
print()
print(response)