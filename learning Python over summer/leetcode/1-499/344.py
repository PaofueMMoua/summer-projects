class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # make it reverse itself and make sure it doesnt reassign to a new spot that just so happens to contain the same thing but backwards.
         # use s[:] to make sure it isnt reassigning it but rather replacing it
          # use s[::-1] to reverse the order of the list 
        # s[:] = s[::-1] 
        s.reverse()
        print(s)


s = ['h','e','l','l','o']
response = Solution().reverseString(s)

print()
print()
print(response)