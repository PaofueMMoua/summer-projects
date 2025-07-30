class Solution:
    def reverseWords(s: str) -> str:
        # divide s by k so you get segments of k length.
        # reverse / flip even numbers from index 0 forwards.
        # take the first few from index 0 to index k -1 then reverse those 
        words = s.split()
        ans = []
        for word in words:
            ans.append(word[::-1])
        return " ".join(ans)
s = "abcdefg"
result = Solution.reverseWords(s)
print()
print()
print()
print()
print(result)