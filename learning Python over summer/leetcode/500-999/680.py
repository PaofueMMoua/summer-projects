class Solution:
    def validPalindrome(self,  s: str) -> bool:
            placeholder1=0
            placeholder2=len(s)-1
            while placeholder1<=placeholder2:
                if s[placeholder1]!=s[placeholder2]:
                    string1=s[:placeholder1]+s[placeholder1+1:]
                    string2=s[:placeholder2]+s[placeholder2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                placeholder1+=1
                placeholder2-=1
            return True
s = "abc"
response = Solution().validPalindrome(s)

print()
print()
print()
print()
print(response)