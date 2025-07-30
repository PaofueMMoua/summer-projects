class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
# get a
# get b
# set a new number
# compare a to b
    # have it do a for loop backwards starting from the last index of a to the first one
     # if a[i] and b[i] are both 1 then i+1 becomes 1 and i becomes 0
      #  do newBinary = '1' + newBinary or 0
       # return the new binary number?
    # convert binary to decimal?
        a = int(a, 2)
        b = int(b, 2)
     # add two numbers?
        a = a+b    
      # covert back to binary?  
        a = bin(a)[2:]
        return a

a = "111"
b = "1"
# a = "1001"
# b = "101"

response = Solution().addBinary(a, b)


print()
print()
print(response)