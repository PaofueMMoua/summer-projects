class Solution:
    def divideString( s: str, k: int, fill: str) -> [str]:
        chunks = [s[i:i + k] for i in range(0, len(s), k)]
        for chunk in range(len(chunks)) :
            if len(chunks[chunk]) != k:
                temp = k - len(chunks[chunk]) 
                chunks[chunk] += (fill*temp)
        return chunks
    
s = "lhq"
k = 83
fill = "p"
a = Solution.divideString(s,k,fill)
print()
print()
print()
print(a)
print()
print()
print()