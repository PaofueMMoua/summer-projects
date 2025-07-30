class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                k=s[i:j]
                if len(k)>=2:
                    if k[0] == k[-1]:
                        l.append(len(k)-2)
        if l:
            return max(l)
        return -1