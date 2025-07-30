class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
# find the last word
    # potentially finding the last word by striping all whitespaces on the right most side? use rstrip()?
        s = s.rstrip()
        print(s)

    #  find the last white space and everything left of it would be removed? use rindex() and rfind in case there are no spaces
        if s.rfind(' ') >= 0:
            lastSpace = s.rindex(' ')
        else:
            lastSpace = 0
      # use that word as the last word. 
        lastWord = s[lastSpace:] 
        if lastWord.find(' ') >= 0:
            lastWord = lastWord.lstrip()
        return(len(lastWord))

# find how long the last word is
    # use index number + 1 to find the length

# return the last word's length


s = "Hello"
# s = "Hello World"
# s = "Hello World Snuggie "
# s = "Hello World Snuggie Is"
# s = "Hello World Snuggie Is Not "
# s = "Hello World Snuggie Is Not Cool"

response = Solution().lengthOfLastWord(s)


print()
print()
print(response)