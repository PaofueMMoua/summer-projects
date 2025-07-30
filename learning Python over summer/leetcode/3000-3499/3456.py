class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) == 1 and k==1:
            return True
        i=1
        count=1
        while i <= len(s)-1:
            if s[i-1] == s[i]:
                count+=1
            else:
                if count == k :
                    return True
                count=1
            i+=1
        if i == len(s) and count ==k :
            return True
        return False