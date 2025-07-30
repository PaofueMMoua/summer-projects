class Solution:
    def countPrefixSuffixPairs( words: List[str]) -> int:
        # get the length of the words
        n = len(words)
        ans = 0
        # loop through every instance of n
        for i in range(n):
            # set the variable to be string 1
            s1 = words[i]
            # check if it is the refix and sufix of all the rest of the words
            for j in range(i + 1, n):
                s2 = words[j]
                if len(s2) < len(s1):
                    continue
                pre = s2[:len(s1)]
                suf = s2[-len(s1):]
                if pre == s1 and suf == s1:
                    ans += 1
        return ans
words = ["a","aba","ababa","aa"]
response = Solution().countPrefixSuffixPairs(words)

print()
print()
print(Solution().findWordsContaining(words))