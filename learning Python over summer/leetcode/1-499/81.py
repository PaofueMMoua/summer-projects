# binary search 
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        low = 0 
        high = len(nums) -1
        mid = 0
        while low <= high:
            mid = high + low // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return True
        return False
    
# using a in statement

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums