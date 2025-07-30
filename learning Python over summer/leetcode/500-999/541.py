class Solution:
    def reverseStr( s: str, k: int) -> str:
        # divide s by k so you get segments of k length.
        # reverse / flip even numbers from index 0 forwards.
        # take the first few from index 0 to index k -1 then reverse those 
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
s = "abcdefg"
k = 2
result = Solution.reverseStr(s, k)
print()
print()
print()
print()
print(result)