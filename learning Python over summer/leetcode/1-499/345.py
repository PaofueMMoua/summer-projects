class Solution:
    def reverseVowels(self, s: str) -> str:
        # get s
        # get all vowels of s aka A E I O U and their index's 
        # could use a dictionary with the key of the index and the value of the vowel.
        # for loop to loop through s to set each thing in the dictionary?
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        sTemp = list(s)
        i,j = 0,len(s)-1
        while i<=j:
            while i<j and s[i] not in vowels:
                i+=1
            while i<j and s[j] not in vowels:
                j-=1
            sTemp[i],sTemp[j] = sTemp[j],sTemp[i]
            i+=1
            j-=1
        return ''.join(sTemp)
s = 'IceCream'
response = Solution().reverseVowels(s)

print()
print()
print(response)