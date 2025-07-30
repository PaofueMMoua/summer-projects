# class Solution:
#     def removeDuplicates(self, nums):
nums = [1,1,1,2,3,4,4,5,6,7,8,9,9]
s = set(nums)
nums[:len(s)] = list(sorted(s))
print(len(s))
    
