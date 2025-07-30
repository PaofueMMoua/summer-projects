class Solution:
    def compress(self, chars: List[str]) -> int:
        # get a empty string s 
        s = ""
        for i in chars:
            if i in s:
                continue
            elif i not in s: 
                s += i
                if chars.count(i) > 1:
                    s += str(chars.count(i))
        s = list(s)
        print(s)
        chars = s 
        # if the length of the group is 1 then add the character to s 
        # if the length of the group isnt 1 then append the character then the group's length. 
        # a 
        
        
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, 
    # be stored in the input character array chars. 
    # Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

