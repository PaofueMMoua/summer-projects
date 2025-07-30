class Solution:
    def isSubstringPresent(s: str) -> bool:
        # make a reverse string
        #  
        reverse = s[::-1]
        st = set()
        for i in range(len(s) - 1):
            st.add(reverse[i : i + 2])
        for i in range(len(s) - 1):
            if s[i : i + 2] in st: return True
        return False
response = Solution().isSubstringPresent(s)

print()
print()
print()
print()
print(Solution().findWordsContaining(words))